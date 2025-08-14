# ♟️ Chess CLI with LLM Opponent

  

An **interactive chess game** in the terminal.

You play using **UCI moves** (e.g., `e2e4`), and your opponent is an **LLM** that selects one **legal move** from a provided list.

The code is clean, modular, and separated into:

  

-  **`core`** → Game logic

-  **`ui`** → Text-based interface

-  **`llm`** → Integration layer with the AI provider

  

---

  

## 📂 Project Structure

  

```

project/

│

├── core/

│ ├── board.py # Board state, move application, notations

│ ├── utils.py # Helpers & piece constants

│ ├── rules.py # Check, mate, stalemate, castling validation

│ └── move_generator.py # Pseudo-legal moves per piece

│

├── llm/

│ ├── adapter.py # Calls my_llm_call(), validates returned move

│ ├── prompt_builder.py # Builds strict prompt with legal UCI list

│ ├── parser.py # Extracts first valid UCI from text

│ └── client_groq.py # Groq client (my_llm_call)

│ # Optional:

│ # client_xai.py # xAI (Grok) client

│ # client_gemini.py # Google Gemini client

│ # client_ollama.py # Local Ollama client

│

├── ui/

│ └── cli.py # Input (UCI), color selection, board display

│

├── game.py # Main loop: turn management, legality checks

└── main.py # Entry point

```

  

> 💡 Add empty `__init__.py` in `core/`, `llm/`, and `ui/` if needed for clean imports.

  

---

  

## ⚙️ Setup

  

**Requirements:**

- Python **3.10+**

- A terminal font that supports Unicode chess symbols (e.g., *Consolas*, *Fira Code*)

  

**Install dependencies:**

```bash

pip  install  requests

```

  

## ▶️ Running the Game

  

```bash

python  main.py

```

  

1.  **Choose color** → `"y"` for white (default), `"n"` for black

2.  **Enter moves** in UCI format (e.g., `e2e4`, `g8f6`)

3. The game will:

- Display the board each turn

- Validate your move

- Call the LLM to select a move for the opponent

- Auto-promote pawns to queens for simplicity

  

---

  

## 🤖 How the LLM Turn Works

  

1.  **Generate legal moves** — The core module computes all safe UCI moves for the current side.

2.  **Prompt building** — `prompt_builder.py` includes:

- Side to move

- ASCII board

- Exact list of legal UCI moves

- Strict instruction: “Return exactly one 4-char UCI move”

3.  **Parse & validate** — `parser.py` extracts the first UCI, and `adapter.py` ensures it’s legal before applying.

  

---

  

## 🌐 LLM Providers

  

###  **Groq** (Recommended — Fast with LLaMA models)

-  **Endpoint:**  `https://api.groq.com/openai/v1/chat/completions`

-  **Model:**  `"llama3-8b-8192"` (or other supported)

-  **Env:**  `GROQ_API_KEY`

  

**Test your key:**

```python

import requests

key = "GROQ_API_KEY"

r = requests.get("https://api.groq.com/openai/v1/models", headers={"Authorization": f"Bearer {key}"})

print(r.status_code, r.json())

```

  

---

  

###  **xAI (Grok)**

-  **Endpoint:**  `https://api.x.ai/v1/chat/completions`

-  **Model:**  `"grok-4-latest"`

-  **Env:**  `XAI_API_KEY`

  

Example `client_xai.py`:

```python

import requests

  

GROQ_API_KEY =  "Your Key here"

  

def my_llm_call(prompt: str) -> str:

if  not GROQ_API_KEY:

raise  RuntimeError("GROQ_API_KEY working.")

url =  "https://api.groq.com/openai/v1/chat/completions"

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

```

  

---

  

###  **Optional Providers**

-  **Google Gemini** → `gemini-1.5-flash-latest`

-  **Ollama (local)** → Runs offline on `localhost:11434`

  

---

  

## 🛠 Troubleshooting

  

-  **401 Unauthorized:** Wrong API key or endpoint (Groq vs xAI mismatch)

-  **LLM returns extra text:**  `parser.py` extracts `[a-h][1-8][a-h][1-8]` and retries if invalid

-  **Unicode issues:** Change terminal font to *Consolas* or *Fira Code*

-  **Promotions:** Currently auto-promotes to queen (can be extended for choice)

  

---

  

## 📌 Tips

- Print the LLM prompt/response during debugging (but **never** log API keys)

- Add stricter reminders if the LLM returns illegal moves

- You can extend this CLI into a **GUI chess app** with minimal core changes