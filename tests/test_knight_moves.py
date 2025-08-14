from core.board import Board
from core.move_generator import get_knight_moves

def print_moves(board, notation):
    row, col = board.notation_to_index(notation)
    moves = get_knight_moves(board, row, col)
    moves_notation = [board.index_to_notation(r, c) for r, c in moves]
    print(f"Knight legal moves for {notation}: {moves_notation}")

def main():
    board = Board()
    print("=== Initial Position ===")
    board.display()

    # Knight at b1 initial
    print("\nKnight moves from b1:")
    print_moves(board, "b1")

    # Move pawn in front of knight to free some moves
    print("\nMove pawn from d2 to d4 to open diagonal")
    board.move_piece_notation("d2", "d4")
    board.display()

    # Knight moves from b1 again
    print("\nKnight moves from b1 after pawn move:")
    print_moves(board, "b1")

    # Move knight from b1 to c3
    print("\nMove knight from b1 to c3")
    board.move_piece_notation("b1", "c3")
    board.display()

    # Knight moves from c3
    print("\nKnight moves from c3:")
    print_moves(board, "c3")

if __name__ == "__main__":
    main()
