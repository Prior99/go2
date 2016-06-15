import websockets
from go2.game_manager import GameManager
from go2.player_manager import PlayerManager
from go2.client import Client

game_manager = GameManager()
player_manager = PlayerManager()

clients = []

def close():
    for client in clients[:]:
        stop_client(client)

async def connected(websocket, path):
    client = Client(websocket)
    start_client(client)
    print('Currently', len(clients), 'clients connected')
    await client.loop()

def start_client(client):
    print('New connection from ', client.socket.remote_address[0])
    client.on('register', player_manager.register)
    client.on('close', lambda: stop_client(client))
    clients.append(client)

def stop_client(client):
    print('Closing connection to', client.socket.remote_address[0])
    client.close()
    clients.remove(client)
    print('Currently', len(clients), 'clients connected')

accept = websockets.serve(connected, 'localhost', 2338)
print('Listening on 0.0.0.0:2338')
