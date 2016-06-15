from marshmallow import Schema, fields, post_load

class MsgRegister:
    def __init__(self, name):
        self.name = name

class RegisterSchema(Schema):
    name = fields.Str()

    @post_load
    def extract(self, data):
        return MsgRegister(data['name'])
