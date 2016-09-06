from marshmallow import Schema, fields

class MsgCreateGame:
    size = fields.Integer()
    opponents = fields.List(fields.Integer)
