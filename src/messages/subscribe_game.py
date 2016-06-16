from marshmallow import Schema, fields, post_load

class MsgSubscribeGame:
    def __init__(self, game):
        self.game = game

class SubscribeGameSchema(Schema):
    game = fields.Integer()

    @post_load
    def extract(self, data):
        return MsgSubscribeGame(data['game'])
