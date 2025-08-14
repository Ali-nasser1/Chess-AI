from core.move_generator import get_legal_moves
from core.utils import is_white_piece, WHITE_KING, BLACK_KING, WHITE_ROOK, BLACK_ROOK


def find_king(board_obj, is_white_king):
    king_piece = WHITE_KING if is_white_king else BLACK_KING

    for row in range(8):
        for col in range(8):
            if board_obj.board[row][col] == king_piece:
                return (row, col)
            
    return None

def is_square_attacked(board_obj, row, col, by_white = True):
    for r in range(8):
        for c in range(8):
            piece = board_obj.board[r][c]

            if piece == "·":
                continue

            piece_color= is_white_piece(piece)
            if piece_color != by_white:
                continue

            possible_moves = get_legal_moves(board_obj, r, c)

            if (row, col) in possible_moves:
                return True
    
    return False

def is_in_check(board_obj, white_king = True):
    king_index = find_king(board_obj, white_king)

    if king_index is None:
        return False
    
    return is_square_attacked(board_obj, king_index[0], king_index[1], by_white = not white_king)

def simulate_move(board_obj, from_pos, to_pos):
    from_row, from_col = from_pos
    to_row, to_col = to_pos

    original_piece = board_obj.board[to_row][to_col]
    piece_moved = board_obj.board[from_row][from_col]

    board_obj.board[to_row][to_col] = piece_moved
    board_obj.board[from_row][from_col] = "·"

    return original_piece, piece_moved

def undo_simulated_move(board_obj, from_pos, to_pos, original_piece, piece_moved):
    from_row, from_col = from_pos
    to_row, to_col = to_pos

    board_obj.board[from_row][from_col] = piece_moved
    board_obj.board[to_row][to_col] = original_piece

def get_all_legal_moves_for_player(board_obj, white_player = True):
    all_moves = []
    for row in range(8):
        for col in range(8):
            piece = board_obj.board[row][col]

            if piece == "·":
                continue

            piece_color= is_white_piece(piece)
            if piece_color != white_player:
                continue

            piece_moves = get_legal_moves(board_obj, row, col)

            for row_move, col_move in piece_moves:
                all_moves.append({
                    "from": (row, col),
                    "to": (row_move, col_move),
                    "piece": piece
                })

    return all_moves

def get_legal_moves_not_in_check(board_obj, row, col):
    piece = board_obj.board[row][col]
    if piece == "·":
        return []
    
    piece_is_white = is_white_piece(piece)
    possible_moves = get_legal_moves(board_obj, row, col)
    legal_moves = []

    for move_row, move_col in possible_moves:
        original_dest, moved_piece = simulate_move(board_obj, (row, col), (move_row, move_col))
        king_in_check = is_in_check(board_obj, white_king=piece_is_white)
        undo_simulated_move(board_obj, (row, col), (move_row, move_col), original_dest, moved_piece)

        if not king_in_check:
            legal_moves.append((move_row, move_col))

    return legal_moves

def has_legal_moves(board_obj, white_player=True):
    for row in range(8):
        for col in range(8):
            piece = board_obj.board[row][col]
            
            if piece == "·":
                continue
            
            piece_color = is_white_piece(piece)
            if piece_color != white_player:
                continue
            
            safe_moves = get_legal_moves_not_in_check(board_obj, row, col)
            
            if len(safe_moves) > 0:
                return True
    
    return False

def get_position_status(board_obj, white_player = True):
    king_in_check = is_in_check(board_obj, white_king=white_player)
    has_moves = has_legal_moves(board_obj, white_player)

    if not has_moves:
        if king_in_check:
            return "checkmate"
        else:
            return "stalemate"
    else:
        if king_in_check:
            return "check"
        else:
            return "normal"
        
def is_game_over(board_obj, white_turn=True):
    status = get_position_status(board_obj, white_turn)

    if status == "checkmate":
        if white_turn:
            return "checkmate_black"
        else:
            return "checkmate_white"
    
    elif status == "stalemate":
        return "stalemate"
    
    else:
        return "ongoing"

def can_castle_kingside(board_obj, white_player=True):
    if white_player:
        if board_obj.white_king_moved or board_obj.white_rook_kingside_moved:
            return False
    else:
        if board_obj.black_king_moved or board_obj.black_rook_kingside_moved:
            return False
    
    king_piece = WHITE_KING if white_player else BLACK_KING
    rook_piece = WHITE_ROOK if white_player else BLACK_ROOK

    king_row = 7 if white_player else 0

    if (board_obj.board[king_row][4] != king_piece or
        board_obj.board[king_row][7] != rook_piece):
        return False
    
    if (board_obj.board[king_row][5] != "·" or 
        board_obj.board[king_row][6] != "·"):
        return False
    
    if is_in_check(board_obj, white_player):
        return False
    
    # check if not move through check
    original_f, _ = simulate_move(board_obj, (king_row, 4), (king_row, 5))
    king_in_check_f = is_in_check(board_obj, white_player)
    undo_simulated_move(board_obj, (king_row, 4), (king_row, 5), original_f, king_piece)

    if king_in_check_f:
        return False
    
    # check if king ends in check
    original_g, _ = simulate_move(board_obj, (king_row, 4), (king_row, 6))
    king_in_check_g = is_in_check(board_obj, white_player)
    undo_simulated_move(board_obj, (king_row, 4), (king_row, 6), original_g, king_piece)

    return not king_in_check_g

def can_castle_queenside(board_obj, white_player=True):
    if white_player:
        if board_obj.white_king_moved or board_obj.white_rook_queenside_moved:
            return False
    else:
        if board_obj.black_king_moved or board_obj.black_rook_queenside_moved:
            return False
    
    king_piece = WHITE_KING if white_player else BLACK_KING
    rook_piece = WHITE_ROOK if white_player else BLACK_ROOK

    king_row = 7 if white_player else 0

    if (board_obj.board[king_row][4] != king_piece or
        board_obj.board[king_row][0] != rook_piece):
        return False
    
    if (board_obj.board[king_row][1] != "·" or 
        board_obj.board[king_row][2] != "·" or
        board_obj.board[king_row][3] != "·"):
        return False
    
    if is_in_check(board_obj, white_player):
        return False
    
    for target_col in [3, 2]:
        original, _ = simulate_move(board_obj, (king_row, 4), (king_row, target_col))
        king_in_check = is_in_check(board_obj, white_player)
        undo_simulated_move(board_obj, (king_row, 4), (king_row, target_col), original, king_piece)
        
        if king_in_check:
            return False
    
    return True