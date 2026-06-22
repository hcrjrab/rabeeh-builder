from app.llm.model_selector import model_selector


class ProviderManager:
    """
    Select provider and model.
    """

    def get_provider_name(
        self,
        provider: str = "auto",
        task: str = "chat",
    ) -> str:

        if provider != "auto":
            return provider

        config = model_selector.select(task)

        return config["provider"]

    def get_model_name(
        self,
        task: str = "chat",
    ) -> str:

        config = model_selector.select(task)

        return config["model"]


provider_manager = ProviderManager()