from main import db

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())

    #extended parent-child relationship
    ChildOf = db.Column(db.Integer, db.ForeignKey("lists.id"), nullable=False)

    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"), nullable=False)

    def __repr__(self):
        return f"<Card {self.title}>"