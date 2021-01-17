from main import ma
from models.Card import Card
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length

class CardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Card

    card_id = ma.String(required=True, validate=Length(min=1))
    user = ma.Nested(UserSchema)


card_schema = CardSchema()
cards_schema = CardSchema(many=True)