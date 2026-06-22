from app.llm.providers.ollama_provider import ollama_provider


class ProviderFactory:
    """
    Factory responsible for returning
    the configured LLM provider.
    """

    def get_provider(self):
        """
        Return the active provider.

        Future providers:
        - OpenRouter
        - OpenAI
        - Gemini
        - Claude
        - Groq
        - DeepSeek
        - Mistral
        """

        return ollama_provider


provider_factory = ProviderFactory()