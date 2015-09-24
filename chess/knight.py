from piece import Piece
from board import Board

class Knight(Piece):
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
        return hash("_".join(["knight", str(self.__posx__), str(self.__posy__)]))

    def __eq__(self, other):
        return self.__hash__() ==  other.__hash__()

    board = property(get_board, set_board)
    color = property(get_color, set_color)
    position = property(get_color, set_color)

    def get_possible_moves(self):
        for x in [2,-2]:
            self.__moves__.extend(self._get_one_off_y_move_(self.get_posx() + x, self.get_posy()))
        for y in [2, -2]:
            self.__moves__.extend(self._get_one_off_x_move_(self.get_posx(),self.get_posy() + y))
        return self._literal_form_possible_moves_()

    def _get_one_off_y_move_(self, x, y):
        moves_list = list()
        for tempy in [y+1, y-1]:
            if self.board.is_within_bounds(x, tempy):
                if self.board.get_pieceAt(x, tempy) is not None:
                    if self.board.get_pieceAt(x, tempy).get_color() != self.get_color():
                        moves_list.append((x, tempy))
                else:
                    moves_list.append((x, tempy))
        return  moves_list

    def _get_one_off_x_move_(self, x, y):
        moves_list = list()
        for tempx in [x+1, x-1]:
            if self.board.is_within_bounds(tempx, y):
                if self.board.get_pieceAt(tempx, y) is not None:
                    if self.board.get_pieceAt(tempx, y).get_color() != self.get_color():
                        moves_list.append((tempx, y))
                else:
                    moves_list.append((tempx, y))
        return  moves_list

    def _literal_form_possible_moves_(self):
        moves_list = list()
        for move in self.__moves__:
            moves_list.append("Knight at " + self.get_position() + " can move to " +
                              self.get_board().convert_array_to_pos(move[0], move[1]))
        return moves_list



