import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models import ProductFlavour


class ProductFlavourRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def create_product_flavours(self, product_flavour_data):
        new_product_flavour = ProductFlavour(
            title=product_flavour_data.title,
            active=product_flavour_data.active,
            product_id=product_flavour_data.product_id,
        )
        self.db.add(new_product_flavour)
        await self.db.commit()
        await self.db.refresh(new_product_flavour)
        return new_product_flavour

    async def get_products_flavours(self):
        results = await self.db.execute(select(ProductFlavour))
        products_flavours = results.scalars().all()
        return products_flavours

    async def get_product_flavour_by_id(self, product_flavour_id: uuid.UUID):
        try:
            query = select(ProductFlavour).filter(ProductFlavour.id == product_flavour_id)
            result = await self.db.execute(query)
            product_flavour_obj = result.scalar_one()
            return product_flavour_obj
        except NoResultFound:
            return None

    async def update_product_flavour(
        self,
        product_flavour_id: uuid.UUID,
        title: str,
    ):
        product_flavour_obj = await self.get_product_flavour_by_id(product_flavour_id)
        if product_flavour_obj:
            product_flavour_obj.title = title
            await self.db.commit()
        return product_flavour_obj

    async def delete_product_flavour(self, product_flavour_id: uuid.UUID):
        product_flavour = await self.get_product_flavour_by_id(product_flavour_id)
        if product_flavour:
            self.db.delete(product_flavour)
            await self.db.commit()
