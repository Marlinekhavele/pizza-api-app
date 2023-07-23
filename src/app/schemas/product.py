from uuid import UUID
from typing import Optional

from pydantic import BaseModel, Field
from app.schemas.enums.product_flavour import Flavour

from app.schemas.enums.product_size import Size

class ProductSchema(BaseModel):
    title: str
    description: str
    price: str


class ProductFlavourSchema(BaseModel):
    title: Optional[Flavour]

    active: str
    product_id: UUID = Field(alias="product_id")


class ProductSizeSchema(BaseModel):
    title:Optional[Size]

    active: str
    product_id: UUID = Field(alias="product_id")
