from app.llm.provider_manager import provider_manager
from app.llm.provider_registry import provider_registry


class ProviderFactory:
    """
    Returns active provider instance.
    """

    def get_provider(
        self,
        provider: str = "auto",
    ):

        provider_name = provider_manager.get_provider_name(
            provider
        )

        return provider_registry.get(provider_name)


provider_factory = ProviderFactory()