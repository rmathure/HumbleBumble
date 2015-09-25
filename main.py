from chess.board import Board
from chess.pawn import Pawn
from chess.knight import Knight
from chess.queen import Queen
from chess.king import King
from chess.bishop import Bishop
from chess.rook import Rook
from chess.exceptions import InvalidInputException
input_file = 'input.txt'


def parse_line(board, line_array):
    retObj = None
    if line_array[0].upper() == "PAWN":
        retObj = Pawn(board,line_array[1][0], line_array[1][1], line_array[2])
    elif line_array[0].upper() == "KNIGHT":
        retObj = Knight(board,line_array[1][0], line_array[1][1], line_array[2])
    elif line_array[0].upper() == "QUEEN":
        retObj = Queen(board,line_array[1][0], line_array[1][1], line_array[2])
    elif line_array[0].upper() == "KING":
        retObj = King(board,line_array[1][0], line_array[1][1], line_array[2])
    elif line_array[0].upper() == "BISHOP":
        retObj = Bishop(board,line_array[1][0], line_array[1][1], line_array[2])
    elif line_array[0].upper() == "ROOK":
        retObj = Rook(board,line_array[1][0], line_array[1][1], line_array[2])
    else:
        raise InvalidInputException("Piece not defined")
    return retObj

if __name__ == '__main__':
    board = Board()
    with open(input_file, 'rb') as fileObj:
        color = fileObj.readline().strip().upper()
        for line in fileObj.readlines():
            line_array = line.strip().split("#")
            if len(line_array) != 3:
                raise InvalidInputException("Invalid input file format")
            parse_line(board, line_array)
    board.get_possible_moves(color)


