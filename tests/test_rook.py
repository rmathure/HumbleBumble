from chess.board import Board
from chess.rook import Rook
from chess.pawn import Pawn
import unittest


class TestRookBase(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rook = Rook(self.board, 'b', '2', 'white')

    def test_base_moves(self):
        result = self.rook.get_possible_moves()
        self.assertEqual(len(result), 14)
        self.assertIn((1,0), self.rook.__moves__)
        self.assertIn((1,2), self.rook.__moves__)
        self.assertIn((1,3), self.rook.__moves__)
        self.assertIn((1,4), self.rook.__moves__)
        self.assertIn((1,5), self.rook.__moves__)
        self.assertIn((1,6), self.rook.__moves__)
        self.assertIn((1,7), self.rook.__moves__)
        self.assertIn((0,1), self.rook.__moves__)
        self.assertIn((2,1), self.rook.__moves__)
        self.assertIn((3,1), self.rook.__moves__)
        self.assertIn((4,1), self.rook.__moves__)
        self.assertIn((5,1), self.rook.__moves__)
        self.assertIn((6,1), self.rook.__moves__)
        self.assertIn((7,1), self.rook.__moves__)


class TestRookBlocked(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rook = Rook(self.board, 'b', '2', 'white')
        self.pawn = Pawn(self.board, 'b', '5', 'white')

    def test_blocked_moves(self):
        result = self.rook.get_possible_moves()
        self.assertEqual(len(result), 10)
        self.assertIn((1,0), self.rook.__moves__)
        self.assertIn((1,2), self.rook.__moves__)
        self.assertIn((1,3), self.rook.__moves__)
        self.assertIn((0,1), self.rook.__moves__)
        self.assertIn((2,1), self.rook.__moves__)
        self.assertIn((3,1), self.rook.__moves__)
        self.assertIn((4,1), self.rook.__moves__)
        self.assertIn((5,1), self.rook.__moves__)
        self.assertIn((6,1), self.rook.__moves__)
        self.assertIn((7,1), self.rook.__moves__)


class TestRookAttackMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rook = Rook(self.board, 'b', '2', 'white')
        self.pawn = Pawn(self.board, 'b', '5', 'black')

    def test_attack_moves(self):
        result = self.rook.get_possible_moves()
        self.assertEqual(len(result), 11)
        self.assertIn((1,0), self.rook.__moves__)
        self.assertIn((1,2), self.rook.__moves__)
        self.assertIn((1,3), self.rook.__moves__)
        self.assertIn((0,1), self.rook.__moves__)
        self.assertIn((2,1), self.rook.__moves__)
        self.assertIn((3,1), self.rook.__moves__)
        self.assertIn((4,1), self.rook.__moves__)
        self.assertIn((5,1), self.rook.__moves__)
        self.assertIn((6,1), self.rook.__moves__)
        self.assertIn((7,1), self.rook.__moves__)
        self.assertIn((1,4), self.rook.__moves__)