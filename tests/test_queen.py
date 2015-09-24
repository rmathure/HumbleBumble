import unittest
from chess.queen import Queen
from chess.board import Board
from chess.pawn import Pawn


class TestQueenBase(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.queen = Queen(self.board, 'b', '2', 'white')

    def test_queen_base(self):
        result = self.queen.get_possible_moves()
        self.assertEqual(len(result), 23)
        self.assertIn((0,2), self.queen.__moves__)
        self.assertIn((2,0), self.queen.__moves__)
        self.assertIn((2,2), self.queen.__moves__)
        self.assertIn((3,3), self.queen.__moves__)
        self.assertIn((4,4), self.queen.__moves__)
        self.assertIn((5,5), self.queen.__moves__)
        self.assertIn((6,6), self.queen.__moves__)
        self.assertIn((7,7), self.queen.__moves__)
        self.assertIn((0,0), self.queen.__moves__)
        self.assertIn((1,0), self.queen.__moves__)
        self.assertIn((1,2), self.queen.__moves__)
        self.assertIn((1,3), self.queen.__moves__)
        self.assertIn((1,4), self.queen.__moves__)
        self.assertIn((1,5), self.queen.__moves__)
        self.assertIn((1,6), self.queen.__moves__)
        self.assertIn((1,7), self.queen.__moves__)
        self.assertIn((0,1), self.queen.__moves__)
        self.assertIn((2,1), self.queen.__moves__)
        self.assertIn((3,1), self.queen.__moves__)
        self.assertIn((4,1), self.queen.__moves__)
        self.assertIn((5,1), self.queen.__moves__)
        self.assertIn((6,1), self.queen.__moves__)
        self.assertIn((7,1), self.queen.__moves__)


class TestQueenBlock(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.queen = Queen(self.board, 'b', '2', 'white')
        self.pawn = Pawn(self.board, 'c', '3', 'white')
        self.another_pawn = Pawn(self.board, 'b', '3', 'white')

    def test_queen_block_move(self):
        result = self.queen.get_possible_moves()
        self.assertEqual(len(result), 11)
        self.assertIn((0,2), self.queen.__moves__)
        self.assertIn((2,0), self.queen.__moves__)
        self.assertIn((0,0), self.queen.__moves__)
        self.assertIn((1,0), self.queen.__moves__)
        self.assertIn((2,1), self.queen.__moves__)
        self.assertIn((3,1), self.queen.__moves__)
        self.assertIn((4,1), self.queen.__moves__)
        self.assertIn((5,1), self.queen.__moves__)
        self.assertIn((6,1), self.queen.__moves__)
        self.assertIn((7,1), self.queen.__moves__)
        self.assertIn((0,1), self.queen.__moves__)


class TestQueenAttack(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.queen = Queen(self.board, 'b', '2', 'white')
        self.pawn = Pawn(self.board, 'c', '3', 'black')
        self.another_pawn = Pawn(self.board, 'b', '3', 'black')

    def test_queen_attack_move(self):
        result = self.queen.get_possible_moves()
        self.assertEqual(len(result), 13)
        self.assertIn((0,2), self.queen.__moves__)
        self.assertIn((2,0), self.queen.__moves__)
        self.assertIn((0,0), self.queen.__moves__)
        self.assertIn((1,0), self.queen.__moves__)
        self.assertIn((2,1), self.queen.__moves__)
        self.assertIn((3,1), self.queen.__moves__)
        self.assertIn((4,1), self.queen.__moves__)
        self.assertIn((5,1), self.queen.__moves__)
        self.assertIn((6,1), self.queen.__moves__)
        self.assertIn((7,1), self.queen.__moves__)
        self.assertIn((0,1), self.queen.__moves__)
        self.assertIn((2,2), self.queen.__moves__)
        self.assertIn((1,2), self.queen.__moves__)

