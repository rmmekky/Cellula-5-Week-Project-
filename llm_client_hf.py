# llm_client_hf.py
import os
import requests

HF_TOKEN = os.environ.get("HF_API_TOKEN")
MODEL_ID = "bigcode/starcoder"

API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def call_huggingface(prompt: str) -> str:
    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.1,
            "max_new_tokens": 300,
            "return_full_text": False
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=200)
    result = response.json()

    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"]

    return str(result)
