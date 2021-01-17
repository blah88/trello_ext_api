from main import db

class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    lists = db.relationship("List", backref="board", lazy="dynamic")

    def __repr__(self):
        return f"<Board {self.title}>"