import asyncio
import websockets
import logging
import json
from message import MessageType, MessageSchema

logger = logging.getLogger('websockets.server')
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())

async def connected(websocket, path):
    print('New connection from ', websocket.remote_address[0])
    data = await websocket.recv()
    message = MessageSchema().load(json.loads(data)).data
    print('Received', message.type, MessageType.REGISTER)
    if message.type == MessageType.REGISTER:
        register = message.data
        print('New user registered with username ', register.username)

loop = asyncio.get_event_loop()
accept = websockets.serve(connected, 'localhost', 2338)
server = loop.run_until_complete(accept)

print('Listening on 0.0.0.0:2338')
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    loop.close()
    print('Goodbye!')

