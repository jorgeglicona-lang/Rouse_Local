from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    message: str
    mode: Optional[str] = "general"  # Puede ser "general" o "coding"
    model: Optional[str] = None      # Opcional, por si se quiere forzar un modelo exacto