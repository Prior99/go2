from common.gamelogic.game import Game

class Room:
    def __init__(self, size, players):
        self.players = players
        self.game = Game(size)
