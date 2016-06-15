import websockets
from go2.client import Client
from go2.player import Player
from go2.database import session

clients = []

def close():
    print('Flushing database...')
    session.flush()
    session.close()
    for client in clients[:]:
        stop_client(client)

async def connected(websocket, path):
    client = Client(websocket)
    start_client(client)
    print('Currently', len(clients), 'clients connected')
    await client.loop()

def add_player(name):
    print('New player with name', name, 'registered')
    player = Player(name=name)
    session.add(player)
    session.commit()

def start_client(client):
    print('New connection from ', client.socket.remote_address[0])
    client.on('register', add_player)
    client.on('close', lambda: stop_client(client))
    clients.append(client)

def stop_client(client):
    print('Closing connection to', client.socket.remote_address[0])
    client.close()
    clients.remove(client)
    print('Currently', len(clients), 'clients connected')

accept = websockets.serve(connected, 'localhost', 2338)
print('Listening on 0.0.0.0:2338')
