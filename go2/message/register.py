from marshmallow import Schema, fields, post_load

class MsgRegister:
    def __init__(self, username):
        self.username = username

class RegisterSchema(Schema):
    username = fields.Str()

    @post_load
    def extract(self, data):
        return MsgRegister(data['username'])
