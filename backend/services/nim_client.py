import requests

from app.config.settings import (
    NVIDIA_API_KEY,
    NVIDIA_BASE_URL,
    MODEL_NAME
)

from app.services.prompt_builder import (
    SYSTEM_PROMPT,
    build_prompt
)

HEADERS = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Content-Type": "application/json"
}

def generate_game(prompt: str):

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": build_prompt(prompt)
            }
        ],
        "temperature": 0.3,
        "top_p": 0.95,
        "max_tokens": 4096,
        "stream": False
    }

    response = requests.post(
        f"{NVIDIA_BASE_URL}/chat/completions",
        headers=HEADERS,
        json=payload
    )

    print(response.status_code)

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]


def repair_game(
    broken_html,
    errors
):

    repair_prompt = f"""
Fix this broken HTML5 game.

Problems:
{errors}

Broken Game:
{broken_html}

Requirements:
- Return ONLY corrected HTML
- Keep game playable
- Fix gameplay logic
- Fix controls
- Fix rendering
- Fix layout
"""

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": repair_prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 4096
    }

    response = requests.post(
        f"{NVIDIA_BASE_URL}/chat/completions",
        headers=HEADERS,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]