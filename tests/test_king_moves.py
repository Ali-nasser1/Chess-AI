from core.board import Board
from core.move_generator import get_king_moves

def print_moves(board, notation):
    row, col = board.notation_to_index(notation)
    moves = get_king_moves(board, row, col)
    moves_notation = [board.index_to_notation(r, c) for r, c in moves]
    print(f"King legal moves for {notation}: {moves_notation}")

def main():
    board = Board()
    print("=== Initial Position ===")
    board.display()

    print("\nKing moves from e1 (initial position):")
    print_moves(board, "e1")

    print("\nClearing squares in front of king at e1")
    board.board[6][3] = '·'  # d2
    board.board[6][4] = '·'  # e2
    board.board[6][5] = '·'  # f2
    board.display()

    print("\nKing moves from e1 after clearing:")
    print_moves(board, "e1")

    print("\nMove king e1 to e2")
    board.move_piece_notation("e1", "e2")
    board.display()

    print("\nKing moves from e2:")
    print_moves(board, "e2")

if __name__ == "__main__":
    main()
