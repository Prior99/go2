import websockets
from src.client import Client
from src.database import session
from src.database.player import Player
from sqlalchemy import exc
import config

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
        print('New player with name', name, 'registered, got id', player.id)
        return player
    except exc.IntegrityError:
        session.rollback()
        return None

def get_player(id):
    return session.query(Player).get(id)

def create_game(size):
    try:
        game = Game(size=size)
        session.add(game)
        session.commit()
        print('New game created. Got id', game.id)
        return game
    except:
        return None

def start_client(client):
    print('New connection from ', client.socket.remote_address[0])
    clients.append(client)

def stop_client(client):
    print('Closing connection to', client.socket.remote_address[0])
    client.close()
    clients.remove(client)
    print('Currently', len(clients), 'clients connected')

accept = websockets.serve(connected, config.host, config.port)
print('Listening on ',config.host,':',config.port)
