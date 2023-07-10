from typing import Optional
from pydantic.networks import PostgresDsn
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV_NAME: str = "local"
    DD_AGENT_HOST: Optional[str] = None
    DD_DOGSTATSD_PORT: Optional[int] = None
    SENTRY_DSN: Optional[str] = None

    # PostgreSQL
    DB_HOST: str = "localhost"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password"
    DB_PORT: int = 5432
    DB_NAME: str = "pizza_api_app"

    @property
    def DB_URL(self) -> str:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            host=self.DB_HOST,
            port=str(self.DB_PORT),
            path=f"/{self.DB_NAME}",
            user=self.DB_USER,
            password=self.DB_PASSWORD,
        )
    
    @property
    def DB_URL_SYNC(self) -> str:
        return PostgresDsn.build(
            scheme="postgresql",
            host=self.DB_HOST,
            port=str(self.DB_PORT),
            path=f"/{self.DB_NAME}",
            user=self.DB_USER,
            password=self.DB_PASSWORD,
        )





settings = Settings()
