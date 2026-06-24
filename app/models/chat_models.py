from typing import Optional
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    session_id: str
    model: Optional[str] = None
    mode: Optional[str] = "general"