"""A module providing configuration variables."""

from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    """A class containing base settings configuration."""
    model_config = SettingsConfigDict(extra="ignore")


class AppConfig(BaseConfig):
    """A class containing oddscalc's configuration."""
    RABBITMQ_HOST: Optional[str] = None
    RABBITMQ_PORT: Optional[str] = None
    RABBITMQ_DEFAULT_USER: Optional[str] = None
    RABBITMQ_DEFAULT_PASS: Optional[str] = None


config = AppConfig()
