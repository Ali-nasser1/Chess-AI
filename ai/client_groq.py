import requests

GROQ_API_KEY = "GROQ_KEY"

def my_llm_call(prompt: str) -> str:
    if not GROQ_API_KEY:
       raise RuntimeError("GROQ_API_KEY working.")
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    response = requests.post(url, headers= headers, json= data)
    response.raise_for_status()
    result = response.json()

    return result["choices"][0]["message"]["content"]