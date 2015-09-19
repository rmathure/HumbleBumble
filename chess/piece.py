

import abc


class Piece(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_possible_moves(self):
        pass

    @abc.abstractmethod
    def __hash__(self):
        pass

    @abc.abstractmethod
    def __eq__(self, other):
        pass

    def get_color(self):
        pass

    def set_color(self):
        pass

    def get_position(self):
        pass

    def set_position(self):
        pass

    def set_board(self):
        pass

    def get_board(self):
        pass

    color = abc.abstractproperty(get_color, set_color)
    position = abc.abstractproperty(get_position, set_position)
    board = abc.abstractproperty(get_board, set_board)