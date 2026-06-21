from sqlalchemy.orm import Session

from app.services.agent_service import agent_service


class ChatService:
    """
    Handles all chat operations.
    """

    def send_message(
        self,
        db: Session,
        conversation_id: int,
        message: str,
    ) -> str:
        """
        Send a message to the AI agent.
        """

        return agent_service.chat(
            db=db,
            conversation_id=conversation_id,
            message=message,
        )


chat_service = ChatService()