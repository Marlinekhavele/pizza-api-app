import logging
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from typing import Generator, Optional
from uuid import UUID

from sentry_sdk import set_tag
from starlette.datastructures import Headers
from starlette.types import ASGIApp, Receive, Scope, Send

logger = logging.getLogger(__name__)
ctx: ContextVar["Context"] = ContextVar("context")


@dataclass(frozen=True)
class Context:
    user_id: UUID
    tenant: str


@contextmanager
def set_context(context: Context) -> Generator:
    token = ctx.set(context)
    try:
        yield
    finally:
        ctx.reset(token)


def get_context(headers: Headers) -> Optional[Context]:
    user_id = headers.get("user_id")
    tenant = headers.get("tenant")
    if user_id and tenant:
        return Context(
            user_id=user_id,
            tenant=tenant,
        )
    return None


class ContextMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":  # pragma: no cover
            await self.app(scope, receive, send)
            return

        headers = Headers(scope=scope)
        context = get_context(headers)
        if context is None:
            return await self.app(scope, receive, send)

        token = ctx.set(context)
        set_tag("tenant", context.tenant)
        try:
            await self.app(scope, receive, send)
        finally:
            ctx.reset(token)
            set_tag("tenant", None)
