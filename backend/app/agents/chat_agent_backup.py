from pathlib import Path

from app.agents.base_agent import BaseAgent
from app.services.ollama_service import ollama_service


SYSTEM_PROMPT = (
    Path(__file__).resolve().parent.parent
    / "prompts"
    / "system_prompt.txt"
)


class ChatAgent(BaseAgent):
    """
    Primary chat agent responsible for
    generating AI responses.
    """

    def __init__(self):
        super().__init__(str(SYSTEM_PROMPT))

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


chat_agent = ChatAgent()