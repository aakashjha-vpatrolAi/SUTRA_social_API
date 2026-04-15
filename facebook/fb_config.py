from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


class FBConfig(BaseSettings):
    FB_RAPIDAPI_KEY: str = ""
    FB_BASE_URL: str = ""
    FB_RAPIDAPI_HOST: str = ""

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[1] / ".env",
        extra="ignore",
        case_sensitive=False,
    )


fb_config = FBConfig()
