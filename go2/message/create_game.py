from marshmallow import Schema, fields

class MsgCreateGame(Schema):
    size = fields.Integer()

