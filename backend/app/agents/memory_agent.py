from sqlalchemy.orm import Session

from app.memory.memory_service import memory_service


class MemoryAgent:
    """
    Loads conversation history from the database.
    """

    def get_context(
        self,
        db: Session,
        conversation_id: int,
        limit: int = 10,
    ) -> str:

        messages = memory_service.get_messages(
            db,
            conversation_id,
        )

        messages = messages[-limit:]

        context = []

        for message in messages:
            context.append(
                f"{message.role}: {message.content}"
            )

        return "\n".join(context)


memory_agent = MemoryAgent()