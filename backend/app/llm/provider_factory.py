from app.llm.provider_registry import provider_registry


class ProviderFactory:
    """
    Returns active provider.
    """

    def get_provider(
        self,
        provider: str = "ollama",
    ):

        return provider_registry.get(provider)


provider_factory = ProviderFactory()