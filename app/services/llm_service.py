from ollama import chat


def ask_model(messages: list[dict], model: str = "qwen2.5:3b") -> str:
    response = chat(
        model=model,
        messages=messages
    )
    return response["message"]["content"]