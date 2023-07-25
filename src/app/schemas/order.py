from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.enums.order import OrderStatus


class OrderSchema(BaseModel):
    customer_id: UUID = Field(alias="customer_id")
    status: Optional[OrderStatus]


class OrderItemSchema(BaseModel):
    order_id: UUID = Field(alias="order_id")
    product_id: UUID = Field(alias="product_id")
    quantity: int
