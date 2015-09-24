
import unittest
from chess.bishop import Bishop
from chess.board import Board
from chess.pawn import Pawn


class TestBishopBase(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.bishop = Bishop(self.board, 'b', '2', 'white')

    def test_base_moves(self):
        result = self.bishop.get_possible_moves()
        self.assertEqual(len(result), 9)
        self.assertIn((0,2), self.bishop.__moves__)
        self.assertIn((2,0), self.bishop.__moves__)
        self.assertIn((2,2), self.bishop.__moves__)
        self.assertIn((3,3), self.bishop.__moves__)
        self.assertIn((4,4), self.bishop.__moves__)
        self.assertIn((5,5), self.bishop.__moves__)
        self.assertIn((6,6), self.bishop.__moves__)
        self.assertIn((7,7), self.bishop.__moves__)
        self.assertIn((0,0), self.bishop.__moves__)


class TestBishopBlocked(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.bishop = Bishop(self.board, 'b', '2', 'white')
        self.pawn = Pawn(self.board, 'c', '3', 'white')

    def test_blocked_moves(self):
        result = self.bishop.get_possible_moves()
        self.assertEqual(len(result), 3)
        self.assertIn((0,2), self.bishop.__moves__)
        self.assertIn((2,0), self.bishop.__moves__)
        self.assertIn((0,0), self.bishop.__moves__)


class TestBishopAttackMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.bishop = Bishop(self.board, 'b', '2', 'white')
        self.pawn = Pawn(self.board, 'c', '3', 'black')

    def test_attack_moves(self):
        result = self.bishop.get_possible_moves()
        self.assertEqual(len(result), 4)
        self.assertIn((0,2), self.bishop.__moves__)
        self.assertIn((2,0), self.bishop.__moves__)
        self.assertIn((0,0), self.bishop.__moves__)
        self.assertIn((2,2), self.bishop.__moves__)
