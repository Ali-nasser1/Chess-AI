from typing import List

UNICODE_TO_FEN = {
    "♙": "P", "♘": "N", "♗": "B", "♖": "R", "♕": "Q", "♔": "K",
    "♟": "p", "♞": "n", "♝": "b", "♜": "r", "♛": "q", "♚": "k",
}

EMPTY_TOKENS = {"·", ".", " "}

def board_to_fen(board_obj) -> str:
    rows_fen: List[str] = []

    for row in range(8):
        empty_count = 0
        rank_parts: List[str] = []
        for col in range(8):
            cell = board_obj.board[row][col]
            if cell in EMPTY_TOKENS:
                empty_count += 1
            else:
                if empty_count:
                    rank_parts.append(str(empty_count))
                    empty_count = 0
                fen_char = UNICODE_TO_FEN.get(cell, None)
                if fen_char is None:
                    empty_count += 1
                else:
                    rank_parts.append(fen_char)
        if empty_count:
            rank_parts.append(str(empty_count))
        rows_fen.append("".join(rank_parts))

    placement = "/".join(rows_fen)

    active = "w" if board_obj.turn == "white" else "b"
    castle_field = board_obj.castling_rights if board_obj.castling_rights else "-"

    fen = f"{placement} {active} {castle_field}"
    return fen



def build_prompt_from_board(board_obj, legal_moves: List[str]) -> str:
    fen = board_to_fen(board_obj)
    legal_str = " ".join(legal_moves)
    print(f"FEN: {fen}")

    prompt = (
    "You are a chess engine playing at a strong human level.\n"
    "Your goal is to choose exactly ONE move that follows these priorities:\n"
    "1. If you can capture an enemy piece without risk of immediate loss, do it.\n"
    "2. If no safe capture is available, choose the strongest positional move.\n"
    "3. Avoid blunders and hanging your own pieces.\n\n"
    f"Position (FEN): {fen}\n\n"
    f"Legal moves (UCI format): {legal_str}\n\n"
    "Rules:\n"
    "- You MUST return exactly one move from the provided list.\n"
    "- Do not invent, skip, or alter moves.\n"
    "- Format: UCI only (e.g., e2e4), no extra text.\n"
    "- If there is absolutely no legal move, return: NO_MOVE\n"
     )
    return prompt
