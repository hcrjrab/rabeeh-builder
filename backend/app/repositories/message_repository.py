from sqlalchemy.orm import Session

from app.database.models import Message
from app.repositories.base_repository import BaseRepository


class MessageRepository(BaseRepository[Message]):
    """
    Repository for Message model.
    """

    def __init__(self, db: Session):
        super().__init__(db, Message)

    def create_message(
        self,
        conversation_id: int,
        role: str,
        content: str,
    ):
        """
        Create a new message.
        """

        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content,
        )

        return self.create(message)

    def get_messages(
        self,
        conversation_id: int,
    ):
        """
        Get all messages for a conversation.
        """

        return (
            self.db.query(Message)
            .filter(
                Message.conversation_id == conversation_id
            )
            .order_by(Message.id.asc())
            .all()
        )

    def get_recent_messages(
        self,
        conversation_id: int,
        limit: int = 10,
    ):
        """
        Get recent messages.
        """

        return (
            self.db.query(Message)
            .filter(
                Message.conversation_id == conversation_id
            )
            .order_by(Message.id.desc())
            .limit(limit)
            .all()
        )

    def delete_message(
        self,
        message_id: int,
    ):
        """
        Delete one message.
        """

        message = self.get(message_id)

        if message:
            self.delete(message)

    def delete_conversation_messages(
        self,
        conversation_id: int,
    ):
        """
        Delete all messages of a conversation.
        """

        (
            self.db.query(Message)
            .filter(
                Message.conversation_id == conversation_id
            )
            .delete()
        )

        self.db.commit()