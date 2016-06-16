from marshmallow import Schema, fields, post_load
from enum import Enum
from messages.create_game import CreateGameSchema
from messages.register import RegisterSchema
from messages.subscribe_game import SubscribeGameSchema
from messages.turn import TurnSchema

class MessageType:
    CREATE_GAME = 'creategame'
    REGISTER = 'register'
    SUBSCRIBE_GAME = 'subscribe'
    TURN = 'turn'
    USERS = 'users'

class Message:
    def __init__(self, type, data=None):
        self.type = type
        self.data = data

class MessageSchema(Schema):
    type = fields.Str()
    payload = fields.Raw()

    @post_load
    def extract(self, data):
        type = data['type']
        schema = (CreateGameSchema() if type == MessageType.CREATE_GAME \
            else RegisterSchema() if type == MessageType.REGISTER \
            else SubscribeGameSchema() if type == MessageType.SUBSCRIBE_GAME \
            else TurnSchema() if type == MessageType.SUBSCRIBE_GAME \
            else None)
        if not schema is None:
            payload = schema.load(data['payload'])
            return Message(type, payload.data)
        return Message(type)
