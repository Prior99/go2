from marshmallow import Schema, fields

class MsgTurn(Schema):
    game = fields.Integer()
    x = fields.Integer()
    y = fields.Integer()
