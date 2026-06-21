from sqlalchemy.orm import Session

from app.agents.chat_agent import chat_agent
from app.agents.memory_agent import memory_agent
from app.agents.planner_agent import planner_agent


class AgentService:
    """
    Main AI Orchestrator.
    """

    def chat(
        self,
        db: Session,
        conversation_id: int,
        message: str,
    ) -> str:

        context = memory_agent.get_context(
            db=db,
            conversation_id=conversation_id,
        )

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