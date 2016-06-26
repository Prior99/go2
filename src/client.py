from src.messages.message import MessageType, MessageSchema
from event_emitter import EventEmitter
import json
import src.server

class Client(EventEmitter):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.terminated = False

    def close(self):
        self.terminated = True
    
    async def send(self, msg):
        msg = json.dumps(msg)
        print('Sending to ', self.socket.remote_address[0], ':', msg)
        await self.socket.send(msg + "\n")

    async def register(self, msg):
        result = server.add_player(**msg)
        if result is None:
            await self.send(False)
        else:
            self.send(result.id)

    async def create_game(self, msg):
        result = server.create_game(**msg)
        for opponent in opponents:
            result.players.append(server.get_player(opponent))
        await self.send(result.id)

    async def loop(self):
        while not self.terminated:
            try:
                data = await self.socket.recv()
                message = MessageSchema().load(json.loads(data)).data
                if message.type == MessageType.REGISTER: await self.register(message.data)
                if message.type == MessageType.CREATE_GAME: await self.create_game(message.data)
            except:
                raise
                break
        self.socket.close()
        self.emit('close')
