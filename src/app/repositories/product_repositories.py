# will handle all my product logic
import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models import Product


class ProductRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def create_product(self, product_data):
        new_product = Product(
            id=product_data.id,
            title=product_data.title,
            description=product_data.description,
            price=product_data.price,
        )
        self.db.add(new_product)
        await self.db.commit()
        await self.db.refresh(new_product)
        return new_product

    async def get_products(self):
        results = await self.db.execute(select(Product))
        products = results.scalars().all()
        return products

    async def get_product_by_id(self, product_id: uuid.UUID):
        try:
            query = select(Product).filter(Product.id == product_id)
            result = await self.db.execute(query)
            product_obj = result.scalar_one()
            return product_obj
        except NoResultFound:
            return None

    async def update_product(
        self, product_id: uuid.UUID, title: str, description: str, price: str
    ):
        product_obj = await self.get_product_by_id(product_id)
        if product_obj:
            product_obj.title = title
            product_obj.description = description
            product_obj.price = price
            await self.db.commit()
        return product_obj

    async def delete_product(self, product_id: uuid.UUID):
        product = await self.get_product_by_id(product_id)
        if product:
            self.db.delete(product)
            await self.db.commit()
        return product
