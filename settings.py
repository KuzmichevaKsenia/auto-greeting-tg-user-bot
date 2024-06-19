from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_ID: int
    API_HASH: str
    SESSION: str = 'main'
    ATTACH_FILE_PATH: str | None = None
    MESSAGE: str = 'Hi!'
    PATTERN: str = '(?i)hi'


settings = Settings()
