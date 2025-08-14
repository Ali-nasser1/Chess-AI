def get_player_move():
    move = input("Enter your move in UCI (e.g., e2e4): ").strip().lower()

    if len(move) != 4:
       raise ValueError("Invalid format. Use UCI like e2e4.")
    return move[:2], move[2:]

def choose_player_color():
    player = input("Play as white? (y/n): ").strip().lower()

    return "white" if player in ("y", "yes", "") else "black"

def display_board(board_obj):
    board_obj.display()
