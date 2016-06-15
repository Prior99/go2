from marshmallow import Schema, fields, post_load

class MsgCreateGame:
    def __init__(self, size):
        self.size = size

class CreateGameSchema:
    size = fields.Integer()

    @post_load
    def extract(self, data):
        return MsgCreateGame(data['size'])
