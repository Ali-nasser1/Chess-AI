from core.utils import *

def get_pawn_moves(board_obj, row, col):
    moves = []
    piece = board_obj.board[row][col]
    # move one step forward
    if piece == WHITE_PAWN:
        if in_bounds(row - 1, col) and board_obj.board[row - 1][col] == '·':
            moves.append((row - 1, col))

            if row == 6 and board_obj.board[row - 2][col] == '·':
                moves.append((row - 2, col))

        # Capture a pawn
        for dc in (-1, 1):
            r, c = row - 1, col + dc
            if in_bounds(r, c):
                target = board_obj.board[r][c]
                if target != '·' and is_black_piece(target):
                    moves.append((r, c))
    
    elif piece == BLACK_PAWN:
        if in_bounds(row + 1, col) and board_obj.board[row + 1][col] == '·':
            moves.append((row + 1, col))

            if row == 1  and board_obj.board[row + 2][col] == '·':
                moves.append((row + 2, col))

        # Capture a pawn
        for dc in (-1, 1):
            r, c = row + 1, col + dc
            if in_bounds(r, c):
                target = board_obj.board[r][c]
                if target != "·" and is_white_piece(target):
                    moves.append((r, c))

    return moves

def get_sliding_moves(board_obj, row, col, directions, is_white):
    moves = []
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while in_bounds(r, c):
            target = board_obj.board[r][c]
            if target == '·':
                moves.append((r, c))
            elif is_enemy_piece(target, is_white):
                moves.append((r, c))
                break
            else:
                break
            r += dr
            c += dc
    return moves

def get_rook_moves(board_obj, row, col):
    piece = board_obj.board[row][col]
    is_white = is_white_piece(piece)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return get_sliding_moves(board_obj, row, col, directions, is_white)

def get_knight_moves(board_obj, row, col):
    moves = []
    piece = board_obj.board[row][col]
    is_white_knight = (piece == WHITE_KNIGHT)
    directions = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2),  (1, 2),
        (2, -1),  (2, 1)]
    
    for dr, dc in directions:
        current_row, current_col= row + dr, col + dc
        if in_bounds(current_row, current_col):
            target = board_obj.board[current_row][current_col]
            if target == '·' or is_enemy_piece(target, is_white_knight):
                moves.append((current_row, current_col))

    return moves

def get_bishop_moves(board_obj, row, col):
    piece = board_obj.board[row][col]
    is_white = is_white_piece(piece)
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    return get_sliding_moves(board_obj, row, col, directions, is_white)

def get_queen_moves(board_obj, row, col):
    piece = board_obj.board[row][col]
    is_white = is_white_piece(piece)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    moves = get_sliding_moves(board_obj, row, col, directions, is_white)
    return moves

def get_king_moves(board_obj, row, col):
    moves = []
    piece = board_obj.board[row][col]
    is_white_king = (piece == WHITE_KING)

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for dr, dc in directions:
        current_row, current_col = row + dr, col + dc
        if in_bounds(current_row, current_col):
            target = board_obj.board[current_row][current_col]
            if target == '·' or is_enemy_piece(target, is_white_king):
                moves.append((current_row, current_col))

    from core.rules import can_castle_kingside, can_castle_queenside
    if can_castle_kingside(board_obj, is_white_king):
        moves.append((row, 6)) 

    if can_castle_queenside(board_obj, is_white_king):
        moves.append((row, 2)) 

    return moves

def get_legal_moves(board_obj, row, col):
    piece = board_obj.board[row][col]
    if piece == WHITE_PAWN or piece == BLACK_PAWN:
        return get_pawn_moves(board_obj, row, col)
    
    if piece == WHITE_ROOK or piece == BLACK_ROOK:
        return get_rook_moves(board_obj, row, col)
    
    if piece == WHITE_KNIGHT or piece == BLACK_KNIGHT:
        return get_knight_moves(board_obj, row, col)
    
    if piece == WHITE_BISHOP or piece == BLACK_BISHOP:
        return get_bishop_moves(board_obj, row, col)
    
    if piece == WHITE_QUEEN or piece == BLACK_QUEEN:
        return get_queen_moves(board_obj, row, col)
    
    if piece == WHITE_KING or piece == BLACK_KING:
        return get_king_moves(board_obj, row, col)
    
    return []