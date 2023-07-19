# will handle all my order logic
from fastapi import Depends
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid
from app.deps import get_db_session
from app.models import Order, OrderItem


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
        self, order_id: uuid.UUID, status: str,
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

#test 
#refactor product sizes
class OrderItemRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    # order items
    async def create_order_item(self, order_item_data):
        new_order_item = OrderItem(
            id=order_item_data.id,
            order_id=order_item_data.order_id,
            product_id=order_item_data.product_id,
            quantity=order_item_data.quantity,
        )
        self.db.add(new_order_item)
        await self.db.commit()
        await self.db.refresh(new_order_item)
        return new_order_item
    
    async def get_orders_items(self):
        results = await self.db.execute(select(OrderItem))
        orders_items = results.scalars().all()
        return orders_items

    async def get_order_items_by_id(self, order_item_id: uuid.UUID):
        try:
            query = select(OrderItem).filter(OrderItem.id == order_item_id)
            result = await self.db.execute(query)
            order_item_obj = result.scalar_one()
            return order_item_obj
        except NoResultFound:
            return None

    async def update_order_items_id(
        self, order_item_id: uuid.UUID, quantity: str,
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
        return order_item_obj