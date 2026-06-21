from sqlalchemy.orm import Session

from app.services.agent_service import agent_service


class ChatService:
    """
    Handles chat business logic.
    """

    def chat(
        self,
        db: Session,
        conversation_id: int,
        message: str,
    ) -> str:

        return agent_service.chat(
            db=db,
            conversation_id=conversation_id,
            message=message,
        )


chat_service = ChatService()