from main import ma
from models.List import List
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length

class ListSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = List

    list_id = ma.String(required=True, validate=Length(min=1))
    user = ma.Nested(UserSchema)


list_schema = ListSchema()
lists_schema = ListSchema(many=True)