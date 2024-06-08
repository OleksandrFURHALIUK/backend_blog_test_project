from functools import lru_cache

#from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import  Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    DB_CONNECTION_STRING: str = Field(default='')
    DB_NAME: str = Field(default='db_name')
    DB_USER: str = Field(default='db_user')
    DB_PASS: str = Field(default='')
    MODE: str = Field(default='dev')
    HOST: str = Field(default='0.0.0.0')
    LISTEN_PORT: int = Field(default=8000)

    # reading values from dotenv file for pydantic V2
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()


settings = get_settings()
