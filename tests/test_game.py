from src.gamelogic.game import Game
from src.gamelogic.board import Board, Color
import pytest

N = Color.NEUTRAL
B = Color.BLACK
W = Color.WHITE

def test_invalid_no_freedom():
    board = Board.from_list([
        N, W, N,
        W, N, W,
        N, W, N
    ])
    game = Game.from_board(board)
    assert not game.place_token((1, 1), Color.BLACK)
    assert len(game.history) == 1

def test_invalid_overwrite():
    board = Board.from_list([W])
    game = Game.from_board(board)
    assert not game.place_token((0, 0), Color.BLACK)
    assert len(game.history) == 1

def test_invalid_ko():
    board = Board.from_list([
        W, B, N,
        N, W, B,
        W, B, N
    ])
    game = Game.from_board(board)
    assert game.place_token((0, 1), Color.BLACK)
    assert len(game.history) == 2
    assert not game.place_token((1, 1), Color.WHITE)
    assert len(game.history) == 2
