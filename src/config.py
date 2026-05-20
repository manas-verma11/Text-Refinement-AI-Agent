from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME:     str = 'openai/gpt-4o'
    OPENAI_API_KEY: str = ''
    API_BASE:       str = ''
    MAX_RETRIES:    int = 2

    class Config:
        env_file = '.env'

settings = Settings()