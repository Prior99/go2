import websockets
from client import Client
from database import session
from database.player import Player
from sqlalchemy import exc

clients = []

def close():
    session.close()
    for client in clients[:]:
        stop_client(client)

async def connected(websocket, path):
    client = Client(websocket)
    start_client(client)
    print('Currently', len(clients), 'clients connected')
    await client.loop()

def add_player(name, secret):
    try:
        player = Player(name=name, secret=secret)
        session.add(player)
        session.commit()
        print('New player with name', name, 'registered')
        return True
    except exc.IntegrityError:
        session.rollback()
        return False

def start_client(client):
    print('New connection from ', client.socket.remote_address[0])
    client.on('register', lambda name, secret, callback: callback(add_player(name, secret)))
    client.on('close', lambda: stop_client(client))
    clients.append(client)

def stop_client(client):
    print('Closing connection to', client.socket.remote_address[0])
    client.close()
    clients.remove(client)
    print('Currently', len(clients), 'clients connected')

accept = websockets.serve(connected, 'localhost', 2338)
print('Listening on 0.0.0.0:2338')
