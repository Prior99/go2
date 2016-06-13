from marshmallow import Schema, fields

class MsgRegister(Schema):
    username = fields.Str()
