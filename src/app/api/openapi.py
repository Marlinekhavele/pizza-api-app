from typing import Dict

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


class OpenApiDocumentation:
    def __init__(self, app: FastAPI):
        self.app = app

    def custom_openapi(self) -> Dict:
        if self.app.openapi_schema:
            return self.app.openapi_schema

        openapi_schema = get_openapi(
            title=self.app.title,
            version=self.app.version,
            description=self.app.description,
            routes=self.app.routes,
            tags=self.app.openapi_tags,
        )

        openapi_schema["components"]["securitySchemes"] = {
            "authorization": {
                "type": "apiKey",
                "in": "header",
                "name": "authorization",
                "description": "API Token returned from mothership login (e.g. 'Token 1234567890')",
            },
            "authorization-host": {
                "type": "apiKey",
                "in": "header",
                "name": "authorization-host",
                "description": "Mothership hostname to authenticate against "
                "(e.g. https://sennder-sennder.stg.sennder.com)",
            },
        }

        openapi_schema["security"] = [{"authorization": [], "authorization-host": []}]

        openapi_schema["servers"] = [
            {
                "url": "https://api.dev.cloud.sennder.com/pizza-api-app",
                "description": "DEV",
            },
            {
                "url": "https://api.cloud.sennder.com/pizza-api-app",
                "description": "PROD",
            },
            {
                "url": "http://localhost:{port}",
                "description": "local",
                "variables": {"port": {"default": 8054}},
            },
        ]
        self.app.openapi_schema = openapi_schema

        return self.app.openapi_schema
