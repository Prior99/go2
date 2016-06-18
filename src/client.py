from messages.message import MessageType, MessageSchema
from event_emitter import EventEmitter
import json

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

    async def register(self, register):
        async def callback(result):
            await self.send(result)
        self.emit('register', **register, callback=callback)

    async def loop(self):
        while not self.terminated:
            try:
                data = await self.socket.recv()
                message = MessageSchema().load(json.loads(data)).data
                if message.type == MessageType.REGISTER: await self.register(message.data)
            except:
                raise
                break
        self.socket.close()
        self.emit('close')
