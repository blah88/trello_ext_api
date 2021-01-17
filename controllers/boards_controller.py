from models.Board import Board
from models.User import User
from main import db
from schemas.BoardSchema import board_schema, boards_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort
from sqlalchemy.orm import joinedload

boards = Blueprint('boards', __name__, url_prefix="/boards")

@boards.route("/", methods=["GET"])
def board_index():
    #Retrieve all boards
    boards = Board.query.options(joinedload("user")).all()
    return jsonify(boards_schema.dump(boards))


@boards.route("/", methods=["POST"])
@jwt_required
def board_create():
    #Create a new board
    board_fields = board_schema.load(request.json)
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    new_board = Board()
    new_board.title = board_fields["title"]

    user.boards.append(new_board)
    
    db.session.commit()
    
    return jsonify(board_schema.dump(new_board))


@boards.route("/<int:id>", methods=["GET"])
def board_show(id):
    #Return a single board
    board = Board.query.get(id)
    return jsonify(board_schema.dump(board))


@boards.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
def board_update(id):
    #Update a board
    board_fields = board_schema.load(request.json)
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")

    boards = Board.query.filter_by(id=id, user_id=user.id)
    
    if boards.count() != 1:
        return abort(401, description="Unauthorized to update this board")

    boards.update(board_fields)
    db.session.commit()

    return jsonify(board_schema.dump(boards[0]))


@boards.route("/<int:id>", methods=["DELETE"])
@jwt_required
def board_delete(id):
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Invalid user")


    board = Board.query.filter_by(id=id, user_id=user.id).first()

    if not board:
        return abort(400)

    db.session.delete(board)
    db.session.commit()

    return jsonify(board_schema.dump(board))
