from app.llm.ollama_provider import ollama_provider


class ProviderFactory:
    """
    Factory responsible for returning
    the configured LLM provider.
    """

    def get_provider(self):
        """
        Return active provider.

        Future:
        - OpenAI
        - Claude
        - Gemini
        - Grok
        """

        return ollama_provider


provider_factory = ProviderFactory()