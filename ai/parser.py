import re

def parse_llm_response(response):
    text = response.strip().lower()
    match = re.search(r"\b([a-h][1-8][a-h][1-8])\b", text)

    if not match:
        raise ValueError("LLM response did not contain a valid UCI move.")
    
    return match.group(1)
