from core.board import Board

board = Board()

print("=== Initial Position ===")
board.display()
print("Current turn:", board.turn)

print("\n=== After moving white pawn e2 -> e4 (notation) ===")
board.move_piece_notation("e2", "e4")
board.display()
print("Current turn:", board.turn)

print("\n=== Move back black pawn e7 -> e5 (notation) ===")
board.move_piece_notation("e7", "e5")
board.display()
print("Current turn:", board.turn)