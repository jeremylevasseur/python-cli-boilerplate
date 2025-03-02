from pydantic_settings import BaseSettings, SettingsConfigDict

from constants import EnvironmentType, Locale


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, validate_default=True)


class Config(BaseConfig):
    DEBUG: int = 0
    DEFAULT_LOCALE: Locale = Locale.EN_US
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    APP_NAME: str = "python-cli-boilerplate"
    RELEASE_VERSION: str = "0.0.1"


config: Config = Config()
