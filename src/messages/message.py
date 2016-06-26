from marshmallow import Schema, fields, post_load
from enum import Enum
from src.messages.create_game import MsgCreateGame
from src.messages.register import MsgRegister
from src.messages.subscribe_game import MsgSubscribeGame
from src.messages.turn import MsgTurn

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
        schema = (MsgCreateGame() if type == MessageType.CREATE_GAME \
            else MsgRegister() if type == MessageType.REGISTER \
            else MsgSubscribeGame() if type == MessageType.SUBSCRIBE_GAME \
            else MsgTurn() if type == MessageType.SUBSCRIBE_GAME \
            else None)
        if not schema is None:
            payload = schema.load(data['payload'])
            return Message(type, payload.data)
        return Message(type)
