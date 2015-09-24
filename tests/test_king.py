import unittest
from chess.king import King
from chess.board import Board
from chess.pawn import Pawn


class TestKingBase(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.king = King(self.board, 'b', '2', 'white')

    def test_queen_base(self):
        result = self.king.get_possible_moves()
        self.assertEqual(len(result), 8)
        self.assertIn((0,0), self.king.__moves__)
        self.assertIn((0,1), self.king.__moves__)
        self.assertIn((0,2), self.king.__moves__)
        self.assertIn((1,0), self.king.__moves__)
        self.assertIn((1,2), self.king.__moves__)
        self.assertIn((2,0), self.king.__moves__)
        self.assertIn((2,1), self.king.__moves__)
        self.assertIn((2,2), self.king.__moves__)

class TestKingBlock(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.king = King(self.board, 'b', '2', 'white')
        self.pawn = Pawn(self.board, 'c', '3', 'white')

    def test_queen_block(self):
        result = self.king.get_possible_moves()
        self.assertEqual(len(result), 7)
        self.assertIn((0,0), self.king.__moves__)
        self.assertIn((0,1), self.king.__moves__)
        self.assertIn((0,2), self.king.__moves__)
        self.assertIn((1,0), self.king.__moves__)
        self.assertIn((1,2), self.king.__moves__)
        self.assertIn((2,0), self.king.__moves__)
        self.assertIn((2,1), self.king.__moves__)


class TestKingAttack(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.king = King(self.board, 'b', '2', 'white')
        self.pawn = Pawn(self.board, 'c', '3', 'black')

    def test_queen_attack(self):
        result = self.king.get_possible_moves()
        self.assertEqual(len(result), 8)
        self.assertIn((0,0), self.king.__moves__)
        self.assertIn((0,1), self.king.__moves__)
        self.assertIn((0,2), self.king.__moves__)
        self.assertIn((1,0), self.king.__moves__)
        self.assertIn((1,2), self.king.__moves__)
        self.assertIn((2,0), self.king.__moves__)
        self.assertIn((2,1), self.king.__moves__)
        self.assertIn((2,2), self.king.__moves__)