from go2.game_manager import GameManager
from go2.player_manager import PlayerManager
from go2.message import MessageType, MessageSchema
from event_emitter import EventEmitter
import json

class Client(EventEmitter):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.terminated = False

    def close(self):
        self.terminated = True

    async def loop(self):
        while not self.terminated:
            try:
                data = await self.socket.recv()
                message = MessageSchema().load(json.loads(data)).data
                print('Received', message.type, MessageType.REGISTER)
                if message.type == MessageType.REGISTER:
                    register = message.data
                    self.emit('register', register.username)
            except:
                break
        self.socket.close()
        self.emit('close')
