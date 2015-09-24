from board import Board
from piece import Piece
from horizontal_moving_piece import get_horizontal_moves
from vertical_moving_piece import get_vertical_moves


class Rook(Piece):
    def __init__(self, board, posx, posy, color):
        self.__color__ = None
        self.__posx__ = None
        self.__posy__ = None
        self.__board__ = board
        self.set_color(color)
        self.set_position(posx, posy)
        self.__moves__ = list()
        self.get_board().register_to_set(self)

    def set_color(self, color):
        self.__color__ = color.upper()

    def set_position(self, posx, posy):
        posx, posy = self.get_board().convert_pos_to_array(posx, int(posy))
        self.__posx__ = posx
        self.__posy__ = posy

    def get_color(self):
        return self.__color__

    def get_position(self):
        return self.get_board().convert_array_to_pos(self.get_posx(), self.get_posy())

    def get_posx(self):
        return self.__posx__

    def get_posy(self):
        return self.__posy__

    def get_board(self):
        return self.__board__

    def set_board(self, board):
        self.__board__ = board

    def __hash__(self):
        return hash("_".join(["rook", str(self.__posx__), str(self.__posy__)]))

    def __eq__(self, other):
        return self.__hash__() ==  other.__hash__()

    board = property(get_board, set_board)
    color = property(get_color, set_color)
    position = property(get_color, set_color)

    def get_possible_moves(self):
        self.__moves__.extend(get_horizontal_moves(self, self.board, self.get_posx(), self.get_posy()))
        self.__moves__.extend(get_vertical_moves(self, self.board, self.get_posx(),self.get_posy()))
        return self._literal_form_possible_moves_()

    def _literal_form_possible_moves_(self):
        moves_list = list()
        for move in self.__moves__:
            moves_list.append("Rook at " + self.get_position() + " can move to " +
                              self.get_board().convert_array_to_pos(move[0], move[1]))
        return moves_list
