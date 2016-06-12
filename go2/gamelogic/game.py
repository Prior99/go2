from go2.gamelogic.board import Board, Color

class Game:
    def __init__(self, size):
        self.current_color = Color.BLACK
        self.history = [Board(size)]

    def place_token(self, position, color):
        if self.current_color != color:
            return False
        next_board = self.current_board.set_color(position, color)
        removed_amount = 0
        for neighbour in next_board.get_neighbours(position):
            if not next_board.is_in_board(neighbour):
                continue
            removal_result = next_board.remove_tokens(neighbour)
            next_board = removal_result.board
            removed_amount += removal_result.amount
        if self.is_turn_valid(next_board, position, color):
            self.history.append(next_board)
            self.turn_made()
            return True
        return False

    def turn_made(self):
        if self.current_color == Color.BLACK:
            self.current_color = Color.WHITE
        else
            self.current_color = Color.BLACK

    def from_board(board):
        game = Game(board.size)
        game.history[0] = board
        return game

    @property
    def current_board(self):
        return self.history[-1]

    def is_ko(self, board):
        if len(self.history) < 2:
            return False
        second_last_board = self.history[-2]
        return second_last_board == board

    def is_turn_valid(self, next_board, position, color):
        if self.current_board.get_color(position) != Color.NEUTRAL:
            return False
        if self.is_ko(next_board):
            return False
        if not next_board.has_freedom(position):
            return False
        return True
