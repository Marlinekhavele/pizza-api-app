from typing import Optional
from pydantic.networks import PostgresDsn
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV_NAME: str = "local"
    DD_AGENT_HOST: Optional[str] = None
    DD_DOGSTATSD_PORT: Optional[int] = None
    SENTRY_DSN: Optional[str] = None

      # PostgreSQL
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_NAME: str

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
