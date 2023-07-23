import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models import OrderItem


class OrderItemRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def create_order_items(self, order_item: OrderItem):
        new_order_item = OrderItem(
            order_id=order_item.order_id,
            product_id=order_item.product_id,
            quantity=order_item.quantity,
        )
        self.db.add(new_order_item)
        await self.db.commit()
        await self.db.refresh(new_order_item)
        return new_order_item

    async def get_order_items_by_id(self, order_item_id: uuid.UUID):
        try:
            query = select(OrderItem).filter(OrderItem.id == order_item_id)
            result = await self.db.execute(query)
            order_item_obj = result.scalar_one()
            return order_item_obj
        except NoResultFound:
            return None

    async def update_order_items_id(
        self,
        order_item_id: uuid.UUID,
        quantity: int,
    ):
        order_item_obj = await self.get_order_items_by_id(order_item_id)
        if order_item_obj:
            order_item_obj.quantity = quantity

            await self.db.commit()
        return order_item_obj

    async def delete_order_items_id(self, order_item_id: uuid.UUID):
        order_item_obj = await self.get_order_items_by_id(order_item_id)
        if order_item_obj:
            self.db.delete(order_item_obj)
            await self.db.commit()
