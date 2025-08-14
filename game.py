from core.board import Board
from core.rules import is_game_over, get_legal_moves_not_in_check
from ui.cli import *
from ai.adapter import get_llm_move
from ai.client_groq import my_llm_call
from core.utils import is_white_piece

def list_legal_uci_moves(board_obj):
    legal_moves = []
    white_to_move = (board_obj.turn == "white")

    for row in range(8):
        for col in range(8):
            piece = board_obj.board[row][col]

            if piece == "·":
                continue

            if is_white_piece(piece) != white_to_move:
                continue

            safe_moves = get_legal_moves_not_in_check(board_obj, row, col)
            from_square = board_obj.index_to_notation(row, col)
            for r, c in safe_moves:
                to_square = board_obj.index_to_notation(r, c)
                legal_moves.append(from_square + to_square)
    
    return legal_moves


def print_game_result(status):
    mapping = {
        "checkmate_white": "Checkmate. White wins.",
        "checkmate_black": "Checkmate. Black wins.",
        "stalemate": "Stalemate. Draw.",
    }

    print(mapping.get(status, f"Game over: {status}"))


def main():
    board = Board()
    user_player_color = choose_player_color()

    while True:
        display_board(board)

        status = is_game_over(board, white_turn= (board.turn == "white"))
        if status != "ongoing":
            print_game_result(status)
            break

        legal_moves = list_legal_uci_moves(board)
        if not legal_moves:
            print("No legal moves.")
            break

        side_to_move = board.turn
        try:
            if side_to_move == user_player_color:
                start, end = get_player_move()
                uci = (start + end)
                if uci not in legal_moves:
                    print("Illegal move. Try again.")
                    continue
            else:
                print("LLM is thinking...")
                uci = get_llm_move(board, legal_moves= legal_moves, llm_call= my_llm_call)

                start, end = uci[:2], uci[2:]
            board.move_piece_notation(start, end)
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()