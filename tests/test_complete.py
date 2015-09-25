import unittest
from chess.pawn import Pawn
from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.board import Board


class TestCompleteSet(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.pawn1 = Pawn(self.board, 'a', '2', 'white')
        self.pawn2 = Pawn(self.board, 'b', '2', 'white')
        self.pawn3 = Pawn(self.board, 'c', '2', 'white')
        self.pawn4 = Pawn(self.board, 'd', '2', 'white')
        self.pawn5 = Pawn(self.board, 'e', '2', 'white')
        self.pawn6 = Pawn(self.board, 'f', '2', 'white')
        self.pawn7 = Pawn(self.board, 'g', '2', 'white')
        self.pawn8 = Pawn(self.board, 'h', '2', 'white')
        self.pawn1b = Pawn(self.board, 'h', '7', 'black')
        self.rook1 = Rook(self.board, 'a', '1', 'white')
        self.rook2 = Rook(self.board, 'h', '1', 'white')
        self.knight1 = Knight(self.board, 'b', '1', 'white')
        self.knight2 = Knight(self.board, 'g', '1', 'white')
        self.bishop1 = Bishop(self.board, 'c', '1', 'white')
        self.bishop1 = Bishop(self.board, 'f', '1', 'white')
        self.queen = Queen(self.board, 'd', '1', 'white')
        self.king = King(self.board, 'e', '1', 'white')

    def test_all_moves(self):
        result = self.board.get_possible_moves('white')
        self.assertEqual(len(result), 20)
        self.assertIn((0,2),self.pawn1.__moves__)
        self.assertIn((0,3),self.pawn1.__moves__)
        self.assertIn((1,2),self.pawn2.__moves__)
        self.assertIn((1,3),self.pawn2.__moves__)
        self.assertIn((2,2),self.pawn3.__moves__)
        self.assertIn((2,3),self.pawn3.__moves__)
        self.assertIn((3,2),self.pawn4.__moves__)
        self.assertIn((3,3),self.pawn4.__moves__)
        self.assertIn((4,2),self.pawn5.__moves__)
        self.assertIn((4,3),self.pawn5.__moves__)
        self.assertIn((5,2),self.pawn6.__moves__)
        self.assertIn((5,3),self.pawn6.__moves__)
        self.assertIn((6,2),self.pawn7.__moves__)
        self.assertIn((6,3),self.pawn7.__moves__)
        self.assertIn((7,2),self.pawn8.__moves__)
        self.assertIn((7,3),self.pawn8.__moves__)
        self.assertIn((0,2), self.knight1.__moves__)
        self.assertIn((2,2), self.knight1.__moves__)
        self.assertIn((5,2), self.knight2.__moves__)
        self.assertIn((7,2), self.knight2.__moves__)


