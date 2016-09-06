from common.gamelogic.board import Board, Color
import pytest

@pytest.fixture
def mock_board():
    N = Color.NEUTRAL
    B = Color.BLACK
    W = Color.WHITE
    board = Board.from_list([
        N, W, W, W, N,
        W, B, B, B, W,
        W, B, N, B, W,
        W, B, B, B, W,
        N, W, W, W, N
    ])
    return board

def test_set_color():
    board = Board(9)
    board2 = board.set_color((3, 3), Color.BLACK)
    assert board.get_color((3, 3)) == Color.NEUTRAL
    assert board2.get_color((3, 3)) == Color.BLACK

def test_get_group(mock_board):
    group = mock_board.get_group((1, 1))
    positions = [(1, 1), (2, 1), (3, 1), (1, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
    assert set(group) == set(positions)

def test_remove_tokens(mock_board):
    board, amount = mock_board.\
        set_color((2, 2), Color.BLACK).\
        remove_tokens((1, 1))
    assert amount == 9
    assert board.count_color(Color.BLACK) == 0

def test_encode(mock_board):
    board = mock_board
    assert board.encode() == 'FKiVpGlYqA'

def test_decode(mock_board):
    board = mock_board
    assert Board.from_encoded('FKiVpGlYqA') == board
