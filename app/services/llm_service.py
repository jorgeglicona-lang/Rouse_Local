import os
from ollama import chat

# Ruta absoluta o relativa al prompt de sistema
PROMPT_PATH = os.path.join(os.path.dirname(__file__), "..", "prompts", "system_prompt.txt")

def load_system_prompt() -> str:
    """Carga la personalidad de Rouse desde el archivo de texto."""
    try:
        with open(PROMPT_PATH, "r", encoding="utf-8") as file:
            return file.read()
    except Exception:
        # Fallback en caso de que ocurra un problema al leer el archivo
        return "Eres Rouse, una asistente técnica personal."

def ask_model(message: str, model_name: str) -> str:
    """Envía el contexto del sistema y el mensaje del usuario a Ollama."""
    system_prompt = load_system_prompt()
    
    response = chat(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )
    return response["message"]["content"]