from exceptions import InvalidInputException, ChessTileOccupiedException, PieceColorNotImplemented

class Board(object):
    def __init__(self):
        self.__board__ = [[None for i in xrange(8)] for j in xrange(8)]
        self.white_set = set()
        self.black_set = set()

    def convert_pos_to_array(self, posx, posy):
        posx = ord(posx.upper()) - 65
        posy = int(posy)
        posy -= 1
        if not self.is_within_bounds(posx, posy):
            raise InvalidInputException("Invalid value for position x or y")
        return posx, posy

    def convert_array_to_pos(self, x, y):
        if not self.is_within_bounds(x, y):
            raise InvalidInputException("Invalid value for position x or y")
        posx = chr(x + 65)
        posy = y + 1
        return posx + str(posy)

    def get_pieceAt(self, x, y):
        if not self.is_within_bounds(x, y):
            return None
        return self.__board__[x][y]

    def is_within_bounds(self, x, y):
        if x in range(0, 8) and y in range(0, 8):
            return True
        else:
            return False

    def register_to_set(self, piece):
        if piece.get_color().upper() == "BLACK":
            self.black_set.add(piece)
        elif piece.get_color().upper() == "WHITE":
            self.white_set.add(piece)
        else:
            raise PieceColorNotImplemented("Color " + piece.get_color() + " is not defined.")
        posx, posy = piece.get_posx(), piece.get_posy()
        if self.__board__[posx][posy] is not None:
            raise ChessTileOccupiedException("Tile " + posx + "," + posy + " already occupied")
        self.__board__[posx][posy] = piece


