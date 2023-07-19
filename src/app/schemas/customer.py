from uuid import UUID

from pydantic import BaseModel


class CustomerSchema(BaseModel):
    id: UUID
    name: str
    email: str
    phone: str
