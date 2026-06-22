import requests

from app.core.config import settings
from app.llm.base_provider import BaseProvider


class OllamaProvider(BaseProvider):
    """
    Ollama LLM Provider
    """

    def chat(
        self,
        prompt: str,
    ) -> str:

        response = requests.post(
            f"{settings.OLLAMA_BASE_URL}/api/generate",
            json={
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]


ollama_provider = OllamaProvider()