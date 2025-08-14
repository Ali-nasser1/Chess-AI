from core.board import Board

print("=== Testing Rook Movement ===")

# Create new board
board = Board()
print("\nInitial position:")
board.display()
print("Current turn:", board.turn)

# Move pawn to free the rook
print("\n=== Moving pawn h2 -> h4 to free the rook ===")
board.move_piece_notation("h2", "h4")
board.display()
print("Current turn:", board.turn)

# Test rook moves from h1
print("\n=== Testing White Rook legal moves from h1 ===")
rook_moves = board.get_legal_moves(7, 7)  # h1 position
move_notations = []
for row, col in rook_moves:
    move_notations.append(board.index_to_notation(row, col))
print(f"Available moves from h1: {move_notations}")
print(f"Number of moves: {len(rook_moves)}")

if len(rook_moves) > 0:
    # Move rook to h3
    print("\n=== Moving White Rook h1 -> h3 ===")
    board.move_piece_notation("h1", "h3")
    board.turn = "white"  # Keep white's turn for demonstration
    board.display()
    print("Current turn:", board.turn)
    
    # Test rook moves from h3
    print("\n=== Testing White Rook legal moves from h3 ===")
    h3_position = board.notation_to_index("h3")
    new_moves = board.get_legal_moves(h3_position[0], h3_position[1])
    new_move_notations = []
    for row, col in new_moves:
        new_move_notations.append(board.index_to_notation(row, col))
    print(f"Available moves from h3: {new_move_notations}")
    print(f"Number of moves: {len(new_moves)}")
else:
    print("No moves available - rook might be blocked")

print("\n=== Rook Test Completed! ===")

# Test rook capture scenario
print("\n=== Testing Rook Capture ===")
board2 = Board()

# Create custom position
board2.board[4][4] = "♖"  # White rook on e4
board2.board[4][6] = "♟"  # Black pawn on g4 (can capture)
board2.board[6][4] = "♟"  # Black pawn on e2 (can capture)
board2.board[4][1] = "♙"  # White pawn on b4 (blocks movement)

print("\nCustom position (White Rook on e4):")
board2.display()

print("\n=== Testing White Rook moves from e4 ===")
capture_moves = board2.get_legal_moves(4, 4)  # e4 position
capture_notations = []
for row, col in capture_moves:
    capture_notations.append(board2.index_to_notation(row, col))
print(f"Available moves from e4: {capture_notations}")
print(f"Number of moves: {len(capture_moves)}")

print("\n✅ All Rook tests completed!")