from core.board import Board
from core.move_generator import get_bishop_moves

def print_moves(board, notation):
    row, col = board.notation_to_index(notation)
    moves = get_bishop_moves(board, row, col)
    moves_notation = [board.index_to_notation(r, c) for r, c in moves]
    print(f"Bishop legal moves for {notation}: {moves_notation}")

def main():
    board = Board()
    print("=== Initial Position ===")
    board.display()

    print("\nClear path for bishop at c1")
    board.board[6][3] = '·'  # d2
    board.board[5][4] = '·'  # e3
    board.display()

    print("\nBishop moves from c1:")
    print_moves(board, "c1")

    print("\nMove bishop c1 to e3")
    board.move_piece_notation("c1", "e3")
    board.display()

    print("\nBishop moves from e3:")
    print_moves(board, "e3")

if __name__ == "__main__":
    main()
