from app.agents.base_agent import BaseAgent
from app.llm.provider_factory import provider_factory


class ChatAgent(BaseAgent):
    """
    Main conversational AI agent.
    Uses the configured LLM provider.
    """

    def __init__(self):
        self.provider = provider_factory.get_provider()

    def generate_response(
        self,
        user_message: str,
        context: str = "",
    ) -> str:
        """
        Generate a response using the active LLM provider.
        """

        if context:
            prompt = f"""
Previous Conversation:
{context}

User:
{user_message}

Assistant:
"""
        else:
            prompt = user_message

        return self.provider.chat(prompt)


chat_agent = ChatAgent()