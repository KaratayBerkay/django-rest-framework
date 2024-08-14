import os
from typing import Set
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

RootPath = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=RootPath + '/.env', env_file_encoding='utf-8', extra='ignore')

    auth_key: str = Field('AUTH_KEY')
    api_key: str = Field('API_KEY')
    api_base_url: str = Field('API_BASE_URL')
    # domains: Set[str] = set()


grab_settings = Settings()
grab_settings_dict = grab_settings.model_dump()
