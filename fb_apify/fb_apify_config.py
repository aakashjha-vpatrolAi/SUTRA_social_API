from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


class ApifyConfig(BaseSettings):
    APIFY_TOKEN: str = ""
    FACEBOOK_PAGE_ACTOR: str = ""

    DEFAULT_MAX_POSTS:int = 10
    DEFAULT_RESULTS_LIMIT:int = 1

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[1] / ".env",
        extra="ignore",
        case_sensitive=False,
    )

apify_settings = ApifyConfig()


