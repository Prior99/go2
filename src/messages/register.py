from marshmallow import Schema, fields

class MsgRegister(Schema):
    name = fields.Str()
    secret = fields.Str()
