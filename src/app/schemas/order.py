from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.enums import Status


class OrderSchema(BaseModel):
    id: UUID
    customer_id: UUID = Field(alias="customer_id")
    status: Status


class OrderItemSchema(BaseModel):
    id: UUID
    order_id: UUID = Field(alias="order_id")
    product_id: UUID = Field(alias="product_id")
    quantity: str
