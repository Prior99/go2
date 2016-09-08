import json
import argparse
import asyncio
from client.connection import Connection

config_file = open('go2.json', 'r')
config = json.loads(config_file.read())

parser = argparse.ArgumentParser(description='Go 2 Commandline interface')
parser.add_argument('command', metavar='COMMAND')
parser.add_argument('--user', type=str)
parser.add_argument('--server', type=str)

args = parser.parse_args()
print(args)

async def register(username, websocket):
    await websocket.send();

asyncio.get_event_loop().run_until_complete(Connection.run())
