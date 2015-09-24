import unittest
from chess.board import Board
from chess.knight import Knight


class TestKnightBase(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.knight = Knight(self.board, 'd', '4', 'white')

    def test_base_moves(self):
        result = self.knight.get_possible_moves()
        self.assertEqual(len(result), 8)
        self.assertIn((2,5), self.knight.__moves__)
        self.assertIn((4,5), self.knight.__moves__)
        self.assertIn((2,1), self.knight.__moves__)
        self.assertIn((4,1), self.knight.__moves__)
        self.assertIn((1,2), self.knight.__moves__)
        self.assertIn((1,4), self.knight.__moves__)
        self.assertIn((5,2), self.knight.__moves__)
        self.assertIn((5,4), self.knight.__moves__)


class TestKnightBlockMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.knight = Knight(self.board, 'd', '4', 'white')
        self.block_knight = Knight(self.board, 'b', '3', 'white')

    def test_block_moves(self):
        result = self.knight.get_possible_moves()
        self.assertEqual(len(result), 7)
        self.assertIn((2,5), self.knight.__moves__)
        self.assertIn((4,5), self.knight.__moves__)
        self.assertIn((2,1), self.knight.__moves__)
        self.assertIn((4,1), self.knight.__moves__)
        self.assertIn((1,4), self.knight.__moves__)
        self.assertIn((5,2), self.knight.__moves__)
        self.assertIn((5,4), self.knight.__moves__)


class TestKnightAttackMoves(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.knight = Knight(self.board, 'd', '4', 'white')
        self.block_knight = Knight(self.board, 'b', '3', 'black')

    def test_attack_moves(self):
        result = self.knight.get_possible_moves()
        self.assertEqual(len(result), 8)
        self.assertIn((2,5), self.knight.__moves__)
        self.assertIn((4,5), self.knight.__moves__)
        self.assertIn((2,1), self.knight.__moves__)
        self.assertIn((4,1), self.knight.__moves__)
        self.assertIn((1,4), self.knight.__moves__)
        self.assertIn((5,2), self.knight.__moves__)
        self.assertIn((5,4), self.knight.__moves__)
        self.assertIn((1,2), self.knight.__moves__)


class TestKnightBounds(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.knight = Knight(self.board, 'a', '4', 'white')

    def test_possible_moves(self):
        result = self.knight.get_possible_moves()
        self.assertEqual(len(result), 4)
        self.assertIn((1,5), self.knight.__moves__)
        self.assertIn((1,1), self.knight.__moves__)
        self.assertIn((2,4), self.knight.__moves__)
        self.assertIn((2,2), self.knight.__moves__)
