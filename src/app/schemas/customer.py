from pydantic import BaseModel
from uuid import UUID

class CustomerSchema(BaseModel):
    id: UUID
    name:str
    email:str
    phone:str