
from chess.board import Board


def get_diagonal_moves(board, piece, x, y):
    moves_list = list()
    moves_list.extend(_get_directional_moves_(board, piece, x, y, 1, -1))
    moves_list.extend(_get_directional_moves_(board, piece, x, y, -1, 1))
    moves_list.extend(_get_directional_moves_(board, piece, x, y, 1, 1))
    moves_list.extend(_get_directional_moves_(board, piece, x, y, -1, -1))
    return moves_list


def _get_directional_moves_(board, piece, posx, posy, offsetx, offsety):
    moves_list = list()
    while True:
        posy += offsety
        posx += offsetx
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

