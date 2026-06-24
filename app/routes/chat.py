from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models.chat_models import ChatRequest
from app.services.llm_service import ask_model
from app.db.database import get_db
from app.db.crud import get_or_create_conversation, add_message, get_last_messages
from app.services.persona_loader import build_system_prompt

router = APIRouter()



def resolve_model(payload: ChatRequest) -> str:
    if payload.model:
        return payload.model

    if payload.mode == "coding":
        return "qwen2.5-coder:7b"

    if payload.mode == "general_llama":
        return "llama3:8b"

    return "dolphin-llama3:8b"


@router.post("/chat")
def chat_with_rouse(payload: ChatRequest, db: Session = Depends(get_db)):
    try:
        model_name = resolve_model(payload)

        conversation = get_or_create_conversation(db, payload.session_id)

        # guardar mensaje del usuario
        add_message(
            db=db,
            conversation_id=conversation.id,
            role="user",
            content=payload.message
        )

        # recuperar historial corto
        history = get_last_messages(db, conversation.id, limit=10)
        system_prompt = build_system_prompt()
        messages = [{"role": "system", "content": system_prompt}]
        for msg in history:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })

        # pedir respuesta al modelo
        reply = ask_model(messages=messages, model=model_name)

        # guardar respuesta del asistente
        add_message(
            db=db,
            conversation_id=conversation.id,
            role="assistant",
            content=reply
        )

        return {
            "assistant": "Rouse",
            "session_id": payload.session_id,
            "model": model_name,
            "reply": reply
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))