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
    def setUp(self):
        self.board = Board()
        self.pawn = Pawn(self.board, 'b', '2', 'white')
        self.black_pawn = Pawn(self.board, 'b', '7', 'black')
    def test_double_step_move(self):
        result = self.pawn.get_possible_moves()
        self.assertIn((1,2), self.pawn.__moves__)
        self.assertIn((1,3), self.pawn.__moves__)
        self.assertIn("Pawn at B2 can move to B3", result)
        self.assertIn("Pawn at B2 can move to B4", result)
        result = self.black_pawn.get_possible_moves()
        self.assertIn((1,5), self.black_pawn.__moves__)
        self.assertIn((1,4), self.black_pawn.__moves__)
        self.assertIn("Pawn at B7 can move to B6", result)
        self.assertIn("Pawn at B7 can move to B5", result)


class TestBlockedSteps(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.pawn = Pawn(self.board, 'b', '2', 'white')
        self.black_pawn = Pawn(self.board, 'b', '7', 'black')
        self.blocking_white_pawn = Pawn(self.board, 'b', '3', 'white')
        self.blocking_black_pawn = Pawn(self.board, 'b', '6', 'white')
        self.another_pawn = Pawn(self.board, 'd', '2', 'white')
        self.another_blocking_pawn = Pawn(self.board, 'd', '4', 'white')

    def test_white_block_moves(self):
        result = self.pawn.get_possible_moves()
        self.assertEqual(len(self.pawn.__moves__), 0)

    def test_black_block_moves(self):
        result = self.black_pawn.get_possible_moves()
        self.assertEqual(len(self.black_pawn.__moves__), 0)

    def test_another_white_pawn(self):
        result = self.another_pawn.get_possible_moves()
        self.assertEqual(len(self.another_pawn.__moves__), 1)
        self.assertIn((3,2), self.another_pawn.__moves__)


class TestAttackSteps(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.pawn = Pawn(self.board, 'a', '2', 'white')
        self.black_pawn = Pawn(self.board, 'b', '4', 'black')
        self.another_black_pawn = Pawn(self.board, 'b', '3', 'black')
        self.test_black_pawn = Pawn(self.board, 'b', '7', 'black')
        self.attack_white_pawn= Pawn(self.board, 'c', '6', 'white')
        self.another_attack_white_pawn = Pawn (self.board, 'c', '5', 'white')

    def test_white_moves(self):
        result = self.pawn.get_possible_moves()
        self.assertEqual(len(self.pawn.__moves__), 4)
        self.assertIn((0, 2), self.pawn.__moves__)
        self.assertIn((0, 3), self.pawn.__moves__)
        self.assertIn((1, 2), self.pawn.__moves__)
        self.assertIn((1, 2), self.pawn.__moves__)

    def test_black_moves(self):
        result = self.test_black_pawn.get_possible_moves()
        self.assertEqual(len(self.test_black_pawn.__moves__), 4)
        self.assertIn((1, 5), self.test_black_pawn.__moves__)
        self.assertIn((1, 4), self.test_black_pawn.__moves__)
        self.assertIn((2, 5), self.test_black_pawn.__moves__)
        self.assertIn((2, 4), self.test_black_pawn.__moves__)


