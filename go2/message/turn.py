from marshmallow import Schema, fields, post_load

class MsgTurn:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y

class TurnSchema(Schema):
    game = fields.Integer()
    x = fields.Integer()
    y = fields.Integer()

    @post_load
    def extract(self, data):
        return MsgTurn(data['game'], data['x'], data['y'])
