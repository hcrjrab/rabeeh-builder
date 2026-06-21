from sqlalchemy.orm import Session

from app.database.models import Conversation, Message


class MemoryService:

    def create_conversation(
        self,
        db: Session,
        title: str = "New Chat",
    ) -> Conversation:

        conversation = Conversation(title=title)

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    def save_message(
        self,
        db: Session,
        conversation_id: int,
        role: str,
        content: str,
    ) -> Message:

        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content,
        )

        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    def get_messages(
        self,
        db: Session,
        conversation_id: int,
    ):

        return (
            db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .order_by(Message.id)
            .all()
        )


memory_service = MemoryService()