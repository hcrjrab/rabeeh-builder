from app.llm.provider_registry import provider_registry


class HealthChecker:
    """
    Simple health checker for registered providers.
    """

    def is_healthy(
        self,
        provider_name: str,
    ) -> bool:

        try:

            provider = provider_registry.get(provider_name)

            # Future:
            # provider.health()

            return provider is not None

        except Exception:

            return False

    def healthy_providers(
        self,
    ) -> list[str]:

        healthy = []

        for provider in provider_registry.list():

            if self.is_healthy(provider):

                healthy.append(provider)

        return healthy


health_checker = HealthChecker()