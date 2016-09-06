from marshmallow import Schema, fields, post_load
from enum import Enum
from common.messages.create_game import MsgCreateGame
from common.messages.register import MsgRegister
from common.messages.subscribe_game import MsgSubscribeGame
from common.messages.turn import MsgTurn

class MessageType:
    CREATE_GAME = 'creategame'
    REGISTER = 'register'
    SUBSCRIBE_GAME = 'subscribe'
    TURN = 'turn'
    USERS = 'users'

class Message:
    def __init__(self, type, id, data=None):
        self.type = type
        self.data = data
        self.id = id

class MessageSchema(Schema):
    type = fields.Str()
    payload = fields.Raw()

    @post_load
    def extract(self, data):
        type = data['type']
        id = data['id']
        schema = (MsgCreateGame() if type == MessageType.CREATE_GAME \
            else MsgRegister() if type == MessageType.REGISTER \
            else MsgSubscribeGame() if type == MessageType.SUBSCRIBE_GAME \
            else MsgTurn() if type == MessageType.SUBSCRIBE_GAME \
            else None)
        if not schema is None:
            payload = schema.load(data['payload'])
            return Message(type, id, payload.data)
        return Message(type, id)
