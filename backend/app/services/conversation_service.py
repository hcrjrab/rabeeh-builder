from sqlalchemy.orm import Session

from app.repositories.conversation_repository import ConversationRepository


class ConversationService:
    """
    Handles conversation business logic.
    """

    def create(
        self,
        db: Session,
        title: str,
    ):
        repo = ConversationRepository(db)

        return repo.create_conversation(title)

    def get_all(
        self,
        db: Session,
    ):
        repo = ConversationRepository(db)

        return repo.list_conversations()

    def get(
        self,
        db: Session,
        conversation_id: int,
    ):
        repo = ConversationRepository(db)

        return repo.get(conversation_id)


conversation_service = ConversationService()