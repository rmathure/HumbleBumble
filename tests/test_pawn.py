import unittest
from chess.board import Board
from chess.pawn import Pawn


class TestPawnInit(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init_pawn(self):
        pawn = Pawn(self.board, 'c', '5', 'white')
        posx, posy = self.board.convert_pos_to_array('c', 5)
        self.assertIsNotNone(self.board.__board__[posx][posy])
        self.assertTrue(pawn in self.board.white_set)
        self.assertFalse(pawn in self.board.black_set)

class TestPawnSingleMove(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.pawn = Pawn(self.board, 'c', '5', 'white')
        self.black_pawn = Pawn(self.board, 'b', '3', 'black')

    def test_single_possible_move(self):
        result = self.pawn.get_possible_moves()
        self.assertIn((2, 5), self.pawn.__moves__)
        self.assertIn("Pawn at C5 can move to C6", result)
        result = self.black_pawn.get_possible_moves()
        self.assertIn((1,1,), self.black_pawn.__moves__)
        self.assertIn("Pawn at B3 can move to B2", result)

class TestDoubleMove(unittest.TestCase):
    def test_double_step_move(self):
        pass