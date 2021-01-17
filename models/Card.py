from main import db

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    list_id = db.Column(db.Integer, db.ForeignKey("list.id"), nullable=False)

    def __repr__(self):
        return f"<Card {self.title}>"