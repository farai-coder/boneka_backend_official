import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "fallback-key")  # fallback only for dev

    class Config:
        env_file = ".env"

settings = Settings()
