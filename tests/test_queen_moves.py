from core.board import Board
from core.move_generator import get_queen_moves

def print_moves(board, notation):
    row, col = board.notation_to_index(notation)
    moves = get_queen_moves(board, row, col)
    moves_notation = [board.index_to_notation(r, c) for r, c in moves]
    print(f"Queen legal moves for {notation}: {moves_notation}")

def main():
    board = Board()
    print("=== Initial Position ===")
    board.display()

    print("\nClear path for queen at d1")
    board.board[6][3] = '·'  # d2
    board.board[5][3] = '·'  # d3
    board.board[6][4] = '·'  # e2
    board.board[5][5] = '·'  # f3
    board.display()

    print("\nQueen moves from d1:")
    print_moves(board, "d1")

    print("\nMove queen d1 to d3")
    board.move_piece_notation("d1", "d3")
    board.display()

    print("\nQueen moves from d3:")
    print_moves(board, "d3")

if __name__ == "__main__":
    main()
