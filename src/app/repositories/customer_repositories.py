# will handle all my customer logic
import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models import Customer


class CustomerRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def create_customer(self, customer_data):
        new_customer = Customer(
            name=customer_data.name,
            phone=customer_data.phone,
            email=customer_data.email,
        )
        self.db.add(new_customer)
        await self.db.commit()
        await self.db.refresh(new_customer)
        return new_customer

    async def get_customers(self):
        results = await self.db.execute(select(Customer))
        customers = results.scalars().all()
        return customers

    async def get_customer_by_id(self, customer_id: uuid.UUID):
        try:
            query = select(Customer).filter(Customer.id == customer_id)
            result = await self.db.execute(query)
            customer_obj = result.scalar_one()
            return customer_obj
        except NoResultFound:
            return None

    async def update_customer(
        self, customer_id: uuid.UUID, name: str, email: str, phone: str
    ):
        customer_obj = await self.get_customer_by_id(customer_id)
        if customer_obj:
            customer_obj.name = name
            customer_obj.email = email
            customer_obj.phone = phone
            await self.db.commit()
        return customer_obj

    async def delete_customer(self, customer_id: uuid.UUID):
        customer_obj = await self.get_customer_by_id(customer_id)
        if customer_obj:
            self.db.delete(customer_obj)
            await self.db.commit()
