from app.llm.config import llm_config


class ProviderManager:

    def get_provider_name(
        self,
        provider="auto",
        task="chat",
    ):

        if provider != "auto":
            return provider

        return llm_config.model(task)["provider"]

    def get_model_name(
        self,
        task="chat",
    ):

        return llm_config.model(task)["model"]


provider_manager = ProviderManager()