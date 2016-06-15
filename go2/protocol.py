from autobahn.asyncio.websocket import WebSocketServerProtocol
from message import MessageType, MessageSchema
from event_emitter import EventEmitter
import json

class Go2Protocol(WebSocketServerProtocol, EventEmitter):
    def onConnect(self):
        print('New connection')

    def onMessage(self, payload, isBinary):
        if isBinary:
            self.disconnect()
            return
        print(payload)
        message = MessageSchema().load(json.loads(payload.decode('utf8'))).data
        if message.type == MessageType.REGISTER:
            register = message.data
            print('New user registered with username ', register.username)
            self.emit('register')

