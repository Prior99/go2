import websockets
from server.connection import Connection
from server.database import session
from server.database.player import Player
from common.gamelogic.board import Board
from common.gamelogic.game import Game
from sqlalchemy import exc
import config

clients = []

def close():
    session.close()
    for client in clients[:]:
        stop_client(client)

async def connected(websocket, path):
    client = Connection(websocket)
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

def validate_player(player_id, secret):
    player = get_player(player_id)
    if not(player):
        return False
    return player.secret == secret

def get_game(id):
    return session.query(Game).get(id)

def get_player(id):
    return session.query(Player).get(id)

def create_game(size, opponents):
    try:
        game = Game(size=size)
        for opponent in opponents:
            game.players.append(get_player(opponent))
        session.add(game)
        session.commit()
        print('New game created. Got id', game.id)
        return game
    except:
        return None

def load_game(db_game):
    boards = list()
    for turn in db_game.turns:
        board = Board.from_encoded(turn.board)
        boards.append(board)
    game = Game.from_boards(boards)
    return game

def add_turn(db_game, board):
    if not(db_game):
        return False
    serialized_board = board.encode()
    turn = Turn(board=serialized_board, turn_number=len(db_game.turns))
    db_game.turns.append(turn)
    session.commit()
    loaded_game = load_game(db_game)
    for client in clients:
        client.turn(game_id, loaded_game)
    return True

def place(game_id, x, y, player_id, secret):
    if not(validate_player(player_id, secret)):
        return False
    db_game = get_game(game_id)
    loaded_game = load_game(db_game)
    for index, opponent in enumerate(db_game.opponents):
        if opponent.id == player_id:
            break
    color = Color(index + 1)
    if not loaded_game.place_token((x, y), color):
        return False
    add_turn(db_game, loaded_game.current_board)
    return True

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
