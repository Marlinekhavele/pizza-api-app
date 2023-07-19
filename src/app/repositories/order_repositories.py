# will handle all my order logic
import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models import Order


class OrderRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def create_order(self, order_data):
        new_order = Order(
            id=order_data.id,
            customer_id=order_data.customer_id,
            status=order_data.status,
        )
        self.db.add(new_order)
        await self.db.commit()
        await self.db.refresh(new_order)
        return new_order

    async def get_orders(self):
        results = await self.db.execute(select(Order))
        orders = results.scalars().all()
        return orders

    async def get_order_by_id(self, order_id: uuid.UUID):
        try:
            query = select(Order).filter(Order.id == order_id)
            result = await self.db.execute(query)
            order_obj = result.scalar_one()
            return order_obj
        except NoResultFound:
            return None

    async def update_order_id(
        self,
        order_id: uuid.UUID,
        status: str,
    ):
        order_obj = await self.get_order_by_id(order_id)
        if order_obj:
            order_obj.status = status

            await self.db.commit()
        return order_obj

    async def delete_order(self, order_id: uuid.UUID):
        order_obj = await self.get_order_by_id(order_id)
        if order_obj:
            self.db.delete(order_obj)
            await self.db.commit()
        return order_obj
