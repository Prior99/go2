from autobahn.asyncio.websocket import WebSocketServerProtocol
from message import Message

class Go2Protocol(WebSocketServerProtocol):
    def on_message(self, payload, isBinary):
        message = Message.load(payload)
