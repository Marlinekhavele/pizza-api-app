from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV_NAME: str = "local"
    DD_AGENT_HOST: Optional[str] = None
    DD_DOGSTATSD_PORT: Optional[int] = None
    SENTRY_DSN: Optional[str] = None


settings = Settings()
