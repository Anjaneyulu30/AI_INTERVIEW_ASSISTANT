from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AI Interview Assistant"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///interview.db"

    GEMINI_API_KEY: str
    GROQ_API_KEY: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()