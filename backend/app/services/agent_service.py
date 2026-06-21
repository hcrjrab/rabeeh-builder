from sqlalchemy.orm import Session

from app.agents.chat_agent import chat_agent
from app.agents.memory_agent import memory_agent
from app.agents.planner_agent import planner_agent


class AgentService:
    """
    Main AI service.
    Controls all AI agents.
    """

    def chat(
        self,
        db: Session,
        conversation_id: int,
        message: str,
    ) -> str:

        # പഴയ conversation context എടുക്കുക
        context = memory_agent.get_context(
            db,
            conversation_id,
        )

        # AI-യിൽ നിന്ന് reply വാങ്ങുക
        return chat_agent.generate_response(
            user_message=message,
            context=context,
        )

    def plan(
        self,
        task: str,
    ) -> str:

        return planner_agent.generate_response(task)


agent_service = AgentService()
