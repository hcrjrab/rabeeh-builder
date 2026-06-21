from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Base interface for all LLM providers.
    """

    @abstractmethod
    def chat(
        self,
        prompt: str,
    ) -> str:
        """
        Send prompt to provider.
        """
        pass
    