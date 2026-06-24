from sqlalchemy.orm import Session

from app.db.models import Conversation, Message


def get_or_create_conversation(db: Session, session_id: str) -> Conversation:
    conversation = (
        db.query(Conversation)
        .filter(Conversation.session_id == session_id)
        .first()
    )

    if conversation:
        return conversation

    conversation = Conversation(session_id=session_id)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation


def add_message(db: Session, conversation_id: int, role: str, content: str) -> Message:
    message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_last_messages(db: Session, conversation_id: int, limit: int = 10) -> list[Message]:
    messages = (
        db.query(Message)
        .filter(Message.conversation_id == conversation_id)
        .order_by(Message.created_at.desc())
        .limit(limit)
        .all()
    )

    return list(reversed(messages))