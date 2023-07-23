from uuid import UUID

from pydantic import BaseModel


class CustomerSchema(BaseModel):
    name: str
    email: str
    phone: str
