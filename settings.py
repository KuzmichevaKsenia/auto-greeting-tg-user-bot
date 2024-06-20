from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_ID: int
    API_HASH: str
    SESSION: str = 'main'
    ATTACH_FILE_PATH: str | None = None
    MESSAGE: str = 'Hi!'
    PATTERN: str = '(?i)hi'

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
