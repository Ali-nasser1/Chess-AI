WHITE_PAWN = "♙"
BLACK_PAWN = "♟"
WHITE_ROOK = "♖"
BLACK_ROOK = "♜"
WHITE_KNIGHT = "♘"
BLACK_KNIGHT = "♞"
WHITE_BISHOP = "♗"
BLACK_BISHOP = "♝"
WHITE_QUEEN = "♕"
BLACK_QUEEN = "♛"
WHITE_KING = "♔"
BLACK_KING = "♚"


# Methods area
def in_bounds(row, col):
    return 0 <= row < 8 and 0 <= col < 8

def is_white_piece(piece):
    return piece in ["♙", "♖", "♘", "♗", "♕", "♔"]

def is_black_piece(piece):
    return piece in ["♟", "♜", "♞", "♝", "♛", "♚"]

def is_enemy_piece(piece, current_player_white):
    if current_player_white:
        return is_black_piece(piece)
    else:
        return is_white_piece(piece)