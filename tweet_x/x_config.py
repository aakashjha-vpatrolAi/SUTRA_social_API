from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


class EnvironmentVariableError(Exception):
    pass


class XConfig(BaseSettings):
    X_BASE_URL: str = "https://api.x.com/2"
    X_BEARER_TOKEN: str = ""
    tweet_REQUEST_TIMEOUT: int = 10

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[1] / ".env",
        extra="ignore",
        case_sensitive=False,
    )


x_config = XConfig()
