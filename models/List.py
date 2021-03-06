from main import db

class List(db.Model):
    __tablename__ = "lists"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    board_id = db.Column(db.Integer, db.ForeignKey("boards.id"), nullable=False)
    cards = db.relationship("Card", backref="list", lazy="dynamic")

    def __repr__(self):
        return f"<List {self.title}>"