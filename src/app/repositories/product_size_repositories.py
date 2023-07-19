import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models import ProductSize


class ProductSizeRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    # sizes
    async def create_product_sizes(self, product_size_data):
        new_product_size = ProductSize(
            id=product_size_data.id,
            title=product_size_data.title,
            active=product_size_data.active,
            product_id=product_size_data.product_id,
        )
        self.db.add(new_product_size)
        await self.db.commit()
        await self.db.refresh(new_product_size)
        return new_product_size

    async def get_products_sizes(self):
        results = await self.db.execute(select(ProductSize))
        products_sizes = results.scalars().all()
        return products_sizes

    async def get_product_size_by_id(self, product_size_id: uuid.UUID):
        try:
            query = select(ProductSize).filter(ProductSize.id == product_size_id)
            result = await self.db.execute(query)
            product_size_obj = result.scalar_one()
            return product_size_obj
        except NoResultFound:
            return None

    async def update_product_size(
        self,
        product_size_id: uuid.UUID,
        title: str,
    ):
        product_size_obj = await self.get_product_size_by_id(product_size_id)
        if product_size_obj:
            product_size_obj.title = title
            await self.db.commit()
        return product_size_obj

    async def delete_product_size(self, product_size_id: uuid.UUID):
        product_size = await self.get_product_by_id(product_size_id)
        if product_size:
            self.db.delete(product_size)
            await self.db.commit()
        return product_size
