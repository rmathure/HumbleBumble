
from board import Board


def get_horizontal_moves(piece, board, posx, posy):
    x = posx
    y = posy
    moves_list = list()
    moves_list.extend(_horizontal_traverse_(board, piece, posx, posy, 1))
    moves_list.extend(_horizontal_traverse_(board, piece, posx, posy, -1))
    return moves_list


def _horizontal_traverse_(board, piece, posx, posy, factor):
    moves_list = list()
    while True:
        posx += factor
        if not board.is_within_bounds(posx, posy):
            break
        if board.get_pieceAt(posx, posy) is not None:
            if board.get_pieceAt(posx, posy).get_color() == piece.get_color():
                break
            else:
                moves_list.append((posx, posy))
                break
        else:
            moves_list.append((posx, posy))
    return moves_list


