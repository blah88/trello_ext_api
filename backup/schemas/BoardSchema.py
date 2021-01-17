from main import ma
from models.Board import Board
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length

class BoardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Board

    board_id = ma.String(required=True, validate=Length(min=1))
    user = ma.Nested(UserSchema)


board_schema = BoardSchema()
boards_schema = BoardSchema(many=True)