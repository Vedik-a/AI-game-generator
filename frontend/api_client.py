import requests

BACKEND_URL = "http://localhost:8000/generate"

def generate_game(prompt: str):

    response = requests.post(
        BACKEND_URL,
        json={
            "prompt": prompt
        }
    )

    response.raise_for_status()

    return response.json()