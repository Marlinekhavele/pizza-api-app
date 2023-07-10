from pydantic import BaseModel,Field
from uuid import UUID
from enum import Enum

class Status(str, Enum):
    DRAFT = "Draft"
    PROCESSING = "Processing"
    CANCELLED = "Cancelled"
    DELIVERED = "Delivered"


class OrderSchema(BaseModel):
    id: UUID
    customer_id:UUID = Field(alias='customer_id')
    status:Status
   

class OrderItemSchema(BaseModel):
    id: UUID
    order_id:UUID= Field(alias='order_id')
    product_id:UUID= Field(alias='product_id')
    quantity: str
  
