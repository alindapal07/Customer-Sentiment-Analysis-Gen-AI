from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.2"

    class Config:
        env_file = ".env"


settings = Settings()
 