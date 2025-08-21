
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str = "fallback-key"  # default fallback only for dev

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",  # Allows extra env vars without validation errors
    )

settings = Settings()

