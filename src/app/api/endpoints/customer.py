from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from app.database.session import SessionLocal
from app.schemas import(CustomerSchema,) 
from app.models import Customer
from sqlalchemy import select
import uuid

router = APIRouter()

#CRUD
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        else:
            await session.commit()



@router.post("/customers/")
async def create_customer(customer: CustomerSchema,db:AsyncSession = Depends(get_db_session)):
    """
    Create a Customer and store it in the database
    """
    new_customer=Customer(id=customer.id,name=customer.name,phone=customer.phone,email=customer.email)
    # print(new_customer.email)
    db.add(new_customer)
    await db.commit()
    await db.refresh(new_customer)
    return new_customer
  
@router.get("/customers/")
async def get_customers(db:AsyncSession = Depends(get_db_session)):
    """
    Get customers that are in the database
    """
    results = await db.execute(select(Customer))
    customers = results.scalars().all()
    return customers

@router.get("/customers/{id}")
async def get_customer_id(id: uuid.UUID,db:AsyncSession = Depends(get_db_session)):
    """
    Get customers that are in the database by id
    """
    customer = await db.execute(select(Customer).filter(Customer.id == id))
    customer_obj = customer.scalar_one_or_none()


    return customer_obj

@router.put("/customers/{id}")
async def update_customer_id(id: uuid.UUID, customer: CustomerSchema, db: AsyncSession = Depends(get_db_session)):
    """
    Update customer details using their ID that is in the database
    """
    db_customer = await db.execute(select(Customer).filter(Customer.id == id))
    customer_obj = db_customer.scalar_one_or_none()

    if customer_obj:
        customer_obj.name = customer.name
        customer_obj.email = customer.email
        customer_obj.phone = customer.phone

        await db.commit()

    return customer_obj

@router.delete("/customers/{id}")
async def delete_customer_id(id: uuid.UUID, db: AsyncSession = Depends(get_db_session)):
    """
    Delete customer details using their UUID that is stored in the database
    """
    customer = await db.execute(select(Customer).filter(Customer.id == id))
    customer_obj = customer.scalar_one_or_none()

    if customer_obj:
        db.delete(customer_obj)
        await db.commit()

    return customer_obj