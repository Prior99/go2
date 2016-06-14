from marshmallow import Schema, fields, post_load
from enum import Enum
from message.create_game import MsgCreateGame
from message.register import MsgRegister
from message.subscribe_game import MsgSubscribeGame
from message.turn import MsgTurn

class MessageType(Enum):
    CREATE_GAME = 'creategame',
    REGISTER = 'register',
    SUBSCRIBE_GAME = 'subscribe',
    TURN = 'turn',
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
            schema.load(self.payload)
            return Message(type, schema.data)
        return Message(type)
