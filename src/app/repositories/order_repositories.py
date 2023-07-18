# will handle all my order logic 
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import  Depends

from app.models import Order
from app.deps import get_db_session

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

