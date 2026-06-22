from pathlib import Path

from app.agents.base_agent import BaseAgent
from app.services.ollama_service import ollama_service

PLANNER_PROMPT = (
    Path(__file__).resolve().parent.parent
    / "prompts"
    / "planner_prompt.txt"
)


class PlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__(str(PLANNER_PROMPT))

    def generate_response(
        self,
        user_message: str,
        context: str = "",
    ) -> str:

        prompt = self.build_prompt(
            user_message=user_message,
            context=context,
        )

        return ollama_service.chat(prompt)


planner_agent = PlannerAgent()