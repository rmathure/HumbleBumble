
from piece import Piece
from board import Board

class Pawn(Piece):
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
        return hash("_".join(["pawn", str(self.__posx__), str(self.__posy__)]))

    def __eq__(self, other):
        return self.__hash__() ==  other.__hash__()

    def get_possible_moves(self):
        if self._is_first_move_():
            self.__moves__.extend(self._get_x_offset_moves_(2))
        else:
            self.__moves__.extend(self._get_x_offset_moves_(1))
        return self._literal_form_possible_moves_()

    def get_moves(self):
        return self.__moves__

    def _literal_form_possible_moves_(self):
        moves_list = list()
        for move in self.__moves__:
            moves_list.append("Pawn at " + self.get_position() + " can move to " +
                              self.get_board().convert_array_to_pos(move[0], move[1]))
        return moves_list

    def _get_multiplier_(self):
        if self.get_color() == "BLACK":
            return -1
        else:
            return 1

    def _get_x_offset_moves_(self, places_to_move):
        moves_list = list()
        moves_made = 0
        multiplier = self._get_multiplier_()
        for x in range(1,places_to_move+1):
            tempx, tempy = self.get_posx(), self.get_posy() + (multiplier*x)
            if tempy < 0 or tempy > 7:
                continue
            if self.get_board().get_pieceAt(tempx, tempy) is not None:
                break
            else:
                moves_list.append((tempx, tempy))
                moves_made += 1
                if moves_made <= places_to_move:
                    moves_list.extend(self._check_for_attack_move_(tempx, tempy))
        return moves_list

    def _check_for_attack_move_(self, tempx, tempy):
        moves_list = list()
        for attackx in [tempx + 1, tempx -1]:
            attacky = tempy
            if self.get_board().get_pieceAt(attackx, attacky) is not None:
                if self.get_board().get_pieceAt(attackx, attacky).get_color() != self.get_color():
                    moves_list.append((attackx, attacky))
        return moves_list

    def _is_first_move_(self):
        if self.get_color() == "WHITE":
            return self.get_posy() == 1
        elif self.get_color() == "BLACK":
            return self.get_posy() == 6

    board = property(get_board, set_board)
    color = property(get_color, set_color)
    position = property(get_color, set_color)


