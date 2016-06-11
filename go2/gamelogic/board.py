from enum import Enum
from copy import deepcopy
from collections import namedtuple
import math

RemovalResult = namedtuple('RemovalResult', ['board', 'amount'])

class Color(Enum):
    NEUTRAL = 0
    BLACK = 1
    WHITE = 2

class Board:
    def __init__(self, size):
        self.state = [Color.NEUTRAL]*(size**2)
        self.size = size

    def from_list(list):
        new_board = Board(int(math.sqrt(len(list))))
        new_board.state = list
        return new_board

    def from_board(original_board):
        new_board = deepcopy(original_board)
        return new_board

    def __eq__(self, other):
        return other.state == self.state

    def __ne__(self, other):
        return other.state != self.state

    def calculate_index(self, position):
        return position[1] * self.size + position[0]

    def set_color(self, position, color):
        new_board = self.clone()
        new_board.state[self.calculate_index(position)] = color
        return new_board

    def get_neighbours(self, position):
        yield (position[0] - 1, position[1])
        yield (position[0] + 1, position[1])
        yield (position[0], position[1] - 1)
        yield (position[0], position[1] + 1)

    def is_in_board(self, position):
        return position[0] >= 0 or position[0] < self.size or position[1] >= 0 or position[1] < self.size

    def count_color(self, color):
        return self.state.count(Color.BLACK)

    def get_group(self, position, color=None, visited=None):
        if visited is None:
            visited = []
        if color is None:
            color = self.get_color(position)
        if position in visited:
            return
        if not self.is_in_board(position):
            return
        visited.append(position)
        my_color = self.get_color(position)
        if my_color == color:
            yield position
            for neighbour in self.get_neighbours(position):
                yield from self.get_group(neighbour, color, visited)

    def has_freedom(self, position):
        for group_position in self.get_group(position):
            for neighbour_position in self.get_neighbours(group_position):
                if self.get_color(neighbour_position) == Color.NEUTRAL:
                    return True
        return False

    def remove_tokens(self, position):
        if self.has_freedom(position):
            return RemovalResult(self, 0)
        next_board = self.clone()
        removed = list(next_board.get_group(position))
        for position in removed:
            next_board.state[self.calculate_index(position)] = Color.NEUTRAL
        return RemovalResult(next_board, len(removed))

    def get_color(self, position):
        return self.state[self.calculate_index(position)]

    def clone(self):
        return Board.from_board(self)

    def __repr__(self):
        return str(self.state)
