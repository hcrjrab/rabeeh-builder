from app.llm.config import llm_config
from app.llm.health_checker import health_checker


class ProviderManager:

    def get_provider_name(
        self,
        provider: str = "auto",
        task: str = "chat",
    ) -> str:

        if provider != "auto":

            if not health_checker.is_healthy(provider):
                raise RuntimeError(
                    f"{provider} is unavailable."
                )

            return provider

        selected = llm_config.model(task)["provider"]

        if health_checker.is_healthy(selected):
            return selected

        raise RuntimeError(
            "No healthy provider available."
        )

    def get_model_name(
        self,
        task: str = "chat",
    ) -> str:

        return llm_config.model(task)["model"]


provider_manager = ProviderManager()