from ai.prompt_builder import *
from ai.parser import *

def get_llm_move(board_obj, legal_moves, llm_call = None, max_retries=2):
    if llm_call is None:
        raise RuntimeError("llm call is not provided!")
    
    prompt = build_prompt_from_board(board_obj, legal_moves)
    last_error = None

    for _ in range(max_retries):
        response_text = llm_call(prompt)
        try:
            move = parse_llm_response(response_text)
            if move in legal_moves:
                return move
            last_error = ValueError(f"LLM returned illegal move: {move}")
        except ValueError as e:
            last_error = e
            
        prompt += "\nRemember: respond with exactly ONE move from the given list, UCI only."
    
    raise last_error or RuntimeError("Failed to obtain valid LLM move.")

