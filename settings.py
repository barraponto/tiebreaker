from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict()
    database_url: str = Field(default="sqlite:///data/db.sqlite")
    openai_api_key: str = Field(default="")
