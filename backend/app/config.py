from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AEC AI Platform"
    app_env: str = "development"
    log_level: str = "INFO"
    database_url: str = "postgresql+psycopg://aec:aec@localhost:5432/aec_ai"
    redis_url: str = "redis://localhost:6379/0"
    cors_origins: list[str] = ["http://localhost:3000"]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
