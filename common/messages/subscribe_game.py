from marshmallow import Schema, fields

class MsgSubscribeGame(Schema):
    game = fields.Integer()
