# intent_classifier.py
import re

def classify_intent(text: str) -> str:
    text = text.lower().strip()

    generate_keywords = [
        "generate", "write code", "create", "implement", "build",
        "make code", "fix code", "correct this", "bug", "solution"
    ]

    explain_keywords = [
        "explain", "what is", "define", "describe", "meaning",
        "how does", "why", "explain this"
    ]

    for k in generate_keywords:
        if k in text:
            return "generate"

    for k in explain_keywords:
        if k in text:
            return "explain"

    # fallback
    if re.search(r"(code|function|python)", text):
        return "generate"

    return "explain"
