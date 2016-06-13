from marshmallow import Schema, fields
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

class Message(Schema):
    type = fields.Str()
    payload = fields.Raw()

    def extract(self):
        schema = (MsgCreateGame() if self.type == MessageType.CREATE_GAME \
            else MsgRegister() if self.type == MessageType.REGISTER \
            else MsgSubscribeGame() if self.type == MessageType.SUBSCRIBE_GAME \
            else MsgTurn() if self.type == MessageType.SUBSCRIBE_GAME \
            else None)
        if not schema is None:
            schema.load(self.payload)
            return schema
        else:
            return None
