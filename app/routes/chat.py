from fastapi import APIRouter, HTTPException
from app.models.chat_models import ChatRequest
from app.services.llm_service import ask_model
from app.config import resolve_model

router = APIRouter()

@router.post("/chat")
def chat_with_rouse(payload: ChatRequest):
    try:
        # Resolvemos qué modelo usar basándonos en el modo o modelo explícito enviado
        target_model = resolve_model(payload.mode, payload.model)
        
        reply = ask_model(payload.message, target_model)
        return {
            "assistant": "Rouse",
            "mode": payload.mode,
            "model": target_model,
            "reply": reply
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))