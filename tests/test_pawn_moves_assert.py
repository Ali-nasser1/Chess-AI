from core.board import Board

def test_promotion():
    b2 = Board()

    b2.board = [["·"] * 8 for _ in range(8)]
    b2.board[1][4] = "♙"  
    b2.turn = "white"

    b2.move_piece_notation("e7", "e8")
    assert b2.board[0][4] == "♕", "Pawn should be promoted to queen"
    assert b2.turn == "black", "Turn should change after move"
