from autobahn.asyncio.websocket import WebSocketServerProtocol
from message import MessageType, MessageSchema
from event_emitter import EventEmitter
import json

class Go2Protocol(WebSocketServerProtocol, EventEmitter):
    def onMessage(self, payload, isBinary):
        if isBinary:
            self.disconnect()
            return
        print(payload)
        message = MessageSchema().load(json.loads(payload.decode('utf8'))).data
        if message.type == MessageType.REGISTER:
            self.emit('register', message.data)

