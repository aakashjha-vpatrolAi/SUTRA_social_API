from __future__ import annotations

from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load env vars for modules that use os.getenv() directly.
load_dotenv(Path(__file__).with_name(".env"))


class EnvironmentVariableError(Exception):
    pass


class Config(BaseSettings):
    DEV_MODE: bool = False
    HOST: str = "0.0.0.0"

    # Server Configuration
    SERVER_PORT: int = 8000
    ALLOWED_PORTS: List[str] = Field(default_factory=list)
    CORS_ALLOWED_ORIGIN: List[str] = Field(default_factory=list, validation_alias="ALLOWED_IPS")

    model_config = SettingsConfigDict(
        env_file=Path(__file__).with_name(".env"),
        extra="ignore",
        case_sensitive=False,
    )


config = Config()
