from core.board import Board
from core.rules import (
     get_position_status,
    is_game_over, has_legal_moves, get_all_legal_moves_for_player,
    can_castle_kingside, can_castle_queenside
)

print("=== Testing Chess Rules ===")

# Test 1: Position Status Function
print("\n=== Test 1: Position Status ===")
board1 = Board()

status = get_position_status(board1, white_player=True)
print(f"Starting position status: {status}")

game_status = is_game_over(board1, white_turn=True)
print(f"Game status: {game_status}")

# Test 2: Has Legal Moves vs Get All Legal Moves
print("\n=== Test 2: Performance Comparison ===")
import time

# Test has_legal_moves (should be fast)
start = time.time()
has_moves = has_legal_moves(board1, white_player=True)
fast_time = time.time() - start

# Test get_all_legal_moves_for_player (slower but more detailed)
start = time.time()
all_moves = get_all_legal_moves_for_player(board1, white_player=True)
detailed_time = time.time() - start

print(f"has_legal_moves(): {has_moves} (took {fast_time:.6f}s)")
print(f"get_all_legal_moves_for_player(): {len(all_moves)} moves (took {detailed_time:.6f}s)")

# Show some moves
print("First 5 legal moves:")
for i, move in enumerate(all_moves[:5]):
    from_notation = board1.index_to_notation(move['from'][0], move['from'][1])
    to_notation = board1.index_to_notation(move['to'][0], move['to'][1])
    print(f"  {i+1}. {move['piece']} {from_notation} → {to_notation}")

# Test 3: Check Detection
print("\n=== Test 3: Check Detection ===")
board2 = Board()

# Create check position
board2.board[7][4] = "♔"  # White king on e1
board2.board[0][4] = "♛"  # Black queen on e8

# Clear path
for row in range(1, 7):
    board2.board[row][4] = "·"

print("Check position:")
board2.display()

status = get_position_status(board2, white_player=True)
print(f"Position status: {status}")

# Test 4: Checkmate
print("\n=== Test 4: Checkmate ===")
board3 = Board()

# Create back-rank mate
for r in range(8):
    for c in range(8):
        board3.board[r][c] = "·"

board3.board[7][0] = "♔"  # White king on a1
board3.board[6][0] = "♙"  # Pawn on a2 (blocks escape)
board3.board[6][1] = "♙"  # Pawn on b2 (blocks escape)  
board3.board[0][0] = "♜"  # Black rook on a8

print("Checkmate position:")
board3.display()

status = get_position_status(board3, white_player=True)
print(f"Position status: {status}")

game_result = is_game_over(board3, white_turn=True)
print(f"Game result: {game_result}")

# Test 5: Stalemate
print("\n=== Test 5: Stalemate ===")
board4 = Board()

# Create stalemate
for r in range(8):
    for c in range(8):
        board4.board[r][c] = "·"

board4.board[7][0] = "♔"  # White king on a1
board4.board[5][1] = "♛"  # Black queen on b3

print("Stalemate position:")
board4.display()

status = get_position_status(board4, white_player=True)
print(f"Position status: {status}")

game_result = is_game_over(board4, white_turn=True)
print(f"Game result: {game_result}")

# Test 6: Castling
print("\n=== Test 6: Castling ===")
board5 = Board()

# Clear pieces for castling
board5.board[7][1] = "·"  # Clear knight
board5.board[7][2] = "·"  # Clear bishop
board5.board[7][3] = "·"  # Clear queen
board5.board[7][5] = "·"  # Clear bishop  
board5.board[7][6] = "·"  # Clear knight

print("Position ready for castling:")
board5.display()

can_king_castle = can_castle_kingside(board5, white_player=True)
can_queen_castle = can_castle_queenside(board5, white_player=True)

print(f"Can castle kingside: {can_king_castle}")
print(f"Can castle queenside: {can_queen_castle}")

# Test 7: Complex Position Analysis
print("\n=== Test 7: Complex Position Analysis ===")
board6 = Board()

# Create interesting middle-game position
board6.move_piece_notation("e2", "e4")
board6.move_piece_notation("e7", "e5")
board6.move_piece_notation("d2", "d4")
board6.move_piece_notation("e5", "d4")

print("After some opening moves:")
board6.display()

white_status = get_position_status(board6, white_player=True)
black_status = get_position_status(board6, white_player=False)

print(f"White status: {white_status}")
print(f"Black status: {black_status}")

white_moves = get_all_legal_moves_for_player(board6, white_player=True)
black_moves = get_all_legal_moves_for_player(board6, white_player=False)

print(f"White has {len(white_moves)} legal moves")
print(f"Black has {len(black_moves)} legal moves")

print("\n✅ All rule tests completed!")