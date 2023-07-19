from uuid import UUID

from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    title: str
    description: str
    price: str


class ProductFlavourSchema(BaseModel):
    title: str
    active: str
    product_id: UUID = Field(alias="product_id")


class ProductSizeSchema(BaseModel):
    title: str
    active: str
    product_id: UUID = Field(alias="product_id")
