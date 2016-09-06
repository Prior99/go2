from src.messages.message import MessageType, MessageSchema
import json
import src.server

class Client:
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.terminated = False
        self.subscribed_games = list()

    def close(self):
        self.terminated = True

    async def send(self, msg):
        msg = json.dumps(msg)
        print('Sending to ', self.socket.remote_address[0], ':', msg)
        await self.socket.send(msg + "\n")

    async def shout(self, msg):
        self.send({ 'type': 'shout', 'data': msg })

    async def answer(self, msg_id, msg):
        self.send({ 'type': 'answer', 'id': id, 'data': msg })

    async def turn(self, game_id, game):
        if game_id in self.subscribed_games:
            self.shout({ 'game': game, 'id': game_id, 'type': 'turn' })

    async def create_game(self, msg_id, msg):
        result = server.create_game(**msg)
        await self.answer(msg_id, result.id)

    async def subscribe_game(self, msg_id, msg):
        existing = not server.get_game(msg.game) is None
        if existing:
            self.subscribed_games.append(msg.game)
        await self.answer(msg_id, existing)

    async def register(self, msg_id, msg):
        result = server.add_player(**msg)
        if result is None:
            await self.send(False)
        else:
            self.answer(msg_id, result.id)

    async def loop(self):
        while not self.terminated:
            try:
                data = await self.socket.recv()
                message = MessageSchema().load(json.loads(data)).data
                if message.type == MessageType.REGISTER: await self.register(message.id, message.data)
                if message.type == MessageType.CREATE_GAME: await self.create_game(message.id, message.data)
                if message.type == MessageType.SUBSCRIBE_GAME: await self.subscribe_game(message.id, message.data)
            except:
                raise
                break
        self.socket.close()
