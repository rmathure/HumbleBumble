import unittest
from chess.board import Board
from chess.piece import Piece
from chess.pawn import Pawn
from chess.exceptions import InvalidInputException

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init(self):
        self.assertEqual(self.board.__board__, [[None for x in range(8)] for y in range(8)])

    def test_convert_pos_to_array(self):
        posx, posy = self.board.convert_pos_to_array('c', 5)
        self.assertEqual(posx, 2)
        self.assertEqual(posy, 4)
        posx, posy = self.board.convert_pos_to_array('h', 1)
        self.assertEqual(posx, 7)
        self.assertEqual(posy, 0)
        self.assertRaises(InvalidInputException, lambda: self.board.convert_pos_to_array('i', 1))
        self.assertRaises(InvalidInputException, lambda: self.board.convert_pos_to_array('a', 9))
        self.assertRaises(InvalidInputException, lambda: self.board.convert_pos_to_array('a', -1))
        self.assertRaises(InvalidInputException, lambda: self.board.convert_pos_to_array('a', 0))
        self.assertRaises(InvalidInputException, lambda: self.board.convert_pos_to_array('i', 0))

    def test_convert_array_to_pos(self):
        posx, posy = self.board.convert_array_to_pos(2, 3)
        self.assertEqual(posx, 'C')
        self.assertEqual(posy, 4)
        self.assertRaises(InvalidInputException, lambda: self.board.convert_array_to_pos(0, 8))
        self.assertRaises(InvalidInputException, lambda: self.board.convert_array_to_pos(-1, 8))
        self.assertRaises(InvalidInputException, lambda: self.board.convert_array_to_pos(-1, 9))


    def test_get_piece_at(self):
        self.board.__board__[1][2] = 1
        self.assertIsNone(self.board.get_pieceAt(0,0))
        self.assertIsNotNone(self.board.get_pieceAt(1,2))
        self.assertIsNone(self.board.get_pieceAt(-1, 0))
        self.assertIsNone(self.board.get_pieceAt(1, 9))


