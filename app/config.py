# app/config.py

# Modelos por defecto asignados a cada modo
DEFAULT_MODELS = {
    "general": "qwen2.5:3b",
    "coding": "qwen2.5-coder:7b"
}

def resolve_model(mode: str, explicit_model: str = None) -> str:
    """
    Resuelve qué modelo usar. Si el usuario pasa un modelo específico, tiene prioridad.
    Si no, se asigna el modelo por defecto del modo elegido.
    """
    if explicit_model:
        return explicit_model
    
    # Si el modo no existe en el diccionario, cae en "general" por defecto
    return DEFAULT_MODELS.get(mode.lower(), DEFAULT_MODELS["general"])