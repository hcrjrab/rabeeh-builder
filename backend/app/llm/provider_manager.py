from app.llm.provider_registry import provider_registry


class ProviderManager:
    """
    Decides which LLM provider should be used.
    """

    DEFAULT_PROVIDER = "ollama"

    def get_provider_name(
        self,
        provider: str = "auto",
    ) -> str:
        """
        Return provider name.
        """

        if provider == "auto":
            return self.DEFAULT_PROVIDER

        if not provider_registry.exists(provider):
            raise ValueError(
                f"Unknown provider: {provider}"
            )

        return provider


provider_manager = ProviderManager()