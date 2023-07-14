import sentry_sdk
from datadog import initialize
from ddtrace import tracer
from ddtrace.contrib.asgi import TraceMiddleware
from ddtrace.contrib.asyncio import context_provider
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware import Middleware

from app.api.api import api_router
from app.api.openapi import OpenApiDocumentation
from app.context import ContextMiddleware
from app.settings import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="pizza-api-app",
    middleware=[Middleware(ContextMiddleware)],

)
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.openapi = OpenApiDocumentation(app).custom_openapi  # type: ignore

if settings.DD_AGENT_HOST:
    initialize(
        statsd_host=settings.DD_AGENT_HOST,
        statsd_port=settings.DD_DOGSTATSD_PORT,
        statsd_constant_tags=[f"env:{settings.ENV_NAME}"],
    )
    # enable asyncio support
    tracer.configure(context_provider=context_provider)
    app.add_middleware(TraceMiddleware)

if settings.SENTRY_DSN:
    sentry_sdk.init(settings.SENTRY_DSN, environment=settings.ENV_NAME)
    app.add_middleware(SentryAsgiMiddleware)

app.include_router(api_router, prefix="/api")
