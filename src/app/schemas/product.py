from uuid import UUID

from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    id: UUID
    title: str
    description: str
    price: str


class ProductFlavourSchema(BaseModel):
    id: UUID
    title: str
    active: str
    product_id: UUID = Field(alias="product_id")


class ProductSizeSchema(BaseModel):
    id: UUID
    title: str
    active: str
    product_id: UUID = Field(alias="product_id")
