next_message_id = 0

queued_messages = {}

async def register(name, secret):
    await send('register', { 'name': name, 'secret': secret })

async def send(type, data):
    next_message_id = next_message_id + 1
    message = { 'id': next_message_id, 'type': type, 'data': data } 

async def run():
    async with websockets.connect(args.server) as websocket:
        data = await websocket.recv()
        print('received', data)
        message = json.loads(data)
