from sqlalchemy.orm import Session

from app.database.models import Conversation
from app.repositories.base_repository import BaseRepository


class ConversationRepository(BaseRepository[Conversation]):
    """
    Repository for Conversation model.
    """

    def __init__(self, db: Session):
        super().__init__(db, Conversation)

    def get_by_title(self, title: str):
        """
        Get a conversation by title.
        """
        return (
            self.db.query(Conversation)
            .filter(Conversation.title == title)
            .first()
        )

    def create_conversation(self, title: str):
        """
        Create a new conversation.
        """
        conversation = Conversation(title=title)
        return self.create(conversation)

    def list_conversations(self):
        """
        Return all conversations.
        """
        return (
            self.db.query(Conversation)
            .order_by(Conversation.id.desc())
            .all()
        )