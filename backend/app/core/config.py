from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Rabeeh Builder"
    PROJECT_VERSION: str = "0.1.0"

    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    OLLAMA_BASE_URL: str = "http://127.0.0.1:11434"
    OLLAMA_MODEL: str = "qwen2.5-coder:7b"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()