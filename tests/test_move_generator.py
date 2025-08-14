import unittest
from core.board import Board
from core.move_generator import (
    get_pawn_moves, get_rook_moves, get_knight_moves, 
    get_bishop_moves, get_queen_moves, get_king_moves
)

class TestMoveGenerator(unittest.TestCase):

    def setUp(self):
        self.board = Board()
    
    def test_pawn_moves(self):
        moves = get_pawn_moves(self.board, 6, 4)
        expected = [(5, 4), (4, 4)]
        self.assertCountEqual(moves, expected)

        moves = get_pawn_moves(self.board, 1, 3)
        expected = [(2, 3), (3, 3)]
        self.assertCountEqual(moves, expected)

    def test_rook_moves(self):
        for r in range(1, 7):
            self.board.board[r][0] = '·'
        moves = get_rook_moves(self.board, 7, 0)
        expected = [(6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)]
        self.assertCountEqual(moves, expected)

    def test_knight_moves(self):
        moves = get_knight_moves(self.board, 7, 1)
        expected = [(5, 0), (5, 2)]
        self.assertCountEqual(moves, expected)

    def test_bishop_moves(self):
        self.board.board[6][3] = '·'
        self.board.board[5][4] = '·'
        self.board.board[4][5] = '·'
        self.board.board[3][6] = '·'
        self.board.board[2][7] = '·'
        moves = get_bishop_moves(self.board, 7, 2)
        expected = [(6, 3), (5, 4), (4, 5), (3, 6), (2, 7)]
        self.assertCountEqual(moves, expected)

    def test_queen_moves(self):
        for r in range(1, 7):
            self.board.board[r][3] = '·'
        for c in range(8):
            if c != 3:
                self.board.board[7][c] = '·'
        self.board.board[6][2] = '·'
        self.board.board[5][1] = '·'
        self.board.board[4][0] = '·'
        self.board.board[6][4] = '·'
        self.board.board[5][5] = '·'
        self.board.board[4][6] = '·'
        self.board.board[3][7] = '·'

        moves = get_queen_moves(self.board, 7, 3)
        expected = [
            (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3),
            (7, 2), (7, 1), (7, 0),
            (7, 4), (7, 5), (7, 6), (7, 7),
            (6, 2), (5, 1), (4, 0),
            (6, 4), (5, 5), (4, 6), (3, 7)
        ]
        self.assertCountEqual(moves, expected)

    def test_king_moves(self):
        moves = get_king_moves(self.board, 7, 4)
        self.assertEqual(moves, [])

        self.board.board[6][3] = '·'
        self.board.board[6][4] = '·'
        self.board.board[6][5] = '·'
        moves = get_king_moves(self.board, 7, 4)
        expected = [(6, 3), (6, 4), (6, 5)]
        self.assertCountEqual(moves, expected)

if __name__ == "__main__":
    unittest.main()
