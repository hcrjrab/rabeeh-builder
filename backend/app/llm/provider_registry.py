from app.llm.base_provider import BaseProvider
from app.llm.providers.ollama_provider import ollama_provider


class ProviderRegistry:
    """
    Registry for all available LLM providers.
    """

    def __init__(self):

        self.providers: dict[str, BaseProvider] = {}

        self.register(
            "ollama",
            ollama_provider,
        )

    def register(
        self,
        name: str,
        provider: BaseProvider,
    ) -> None:

        self.providers[name.lower()] = provider

    def get(
        self,
        name: str,
    ) -> BaseProvider:

        provider = self.providers.get(name.lower())

        if provider is None:
            raise ValueError(
                f"Provider '{name}' is not registered."
            )

        return provider

    def exists(
        self,
        name: str,
    ) -> bool:

        return name.lower() in self.providers

    def list(self) -> list[str]:

        return sorted(self.providers.keys())


provider_registry = ProviderRegistry()