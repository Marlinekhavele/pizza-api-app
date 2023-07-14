from uuid import UUID
from app.schemas.enums import Status
from pydantic import BaseModel, Field


class OrderSchema(BaseModel):
    id: UUID
    customer_id: UUID = Field(alias="customer_id")
    status: Status


class OrderItemSchema(BaseModel):
    id: UUID
    order_id: UUID = Field(alias="order_id")
    product_id: UUID = Field(alias="product_id")
    quantity: str
