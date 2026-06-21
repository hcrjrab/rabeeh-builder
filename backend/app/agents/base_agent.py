from abc import ABC, abstractmethod
from pathlib import Path


class BaseAgent(ABC):
    """
    Base class for all Rabeeh AI agents.
    """

    def __init__(self, prompt_file: str):
        self.prompt_file = Path(prompt_file)
        self.system_prompt = self.load_system_prompt()

    def load_system_prompt(self) -> str:
        """
        Load the system prompt from a text file.
        """
        if not self.prompt_file.exists():
            return ""

        return self.prompt_file.read_text(
            encoding="utf-8"
        ).strip()

    def build_prompt(
        self,
        user_message: str,
        context: str = "",
    ) -> str:
        """
        Build the final prompt.
        """
        prompt = self.system_prompt

        if context:
            prompt += f"\n\nConversation:\n{context}"

        prompt += f"\n\nUser:\n{user_message}"

        return prompt

    @abstractmethod
    def generate_response(
        self,
        user_message: str,
        context: str = "",
    ) -> str:
        """
        Generate a response.
        """
        raise NotImplementedError