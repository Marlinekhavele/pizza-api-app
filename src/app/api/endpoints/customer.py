import uuid

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models import Customer
from app.repositories.customer_repositories import CustomerRepository
from app.schemas import CustomerSchema

router = APIRouter()

# CRUD Operation


@router.post("/customers/")
async def create_customer(
    customer: CustomerSchema,
    customer_repo: CustomerRepository = Depends(CustomerRepository),
):
    """
    Create a Customer and store it in the database
    """
    new_customer = await customer_repo.create_customer(customer)
    return new_customer


@router.get("/customers/")
async def get_customers(repo: CustomerRepository = Depends(CustomerRepository)):
    """
    Get customers that are in the database
    """
    return await repo.get_customers()


@router.get("/customers/{id}")
async def get_customer_id(repo: CustomerRepository = Depends(CustomerRepository)):
    """
    Get customers that are in the database by id
    """
    return await repo.get_customer_by_id(id)


@router.put("/customers/{id}")
async def update_customer_id(
    id: uuid.UUID, customer: CustomerSchema, db: AsyncSession = Depends(get_db_session)
):
    """
    Update customer details using their ID that is in the database
    """
    db_customer = await db.execute(select(Customer).filter(Customer.id == id))
    # retrieves the single result row from the executed query, if any.
    # If there are no results, it returns None.
    # This line assumes that only one customer with the given UUID exists in the database.

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
    # retrieves the single result row from the executed query if any. I
    # f there are no results, it returns None.
    customer_obj = customer.scalar_one_or_none()

    if customer_obj:
        db.delete(customer_obj)
        await db.commit()

    return customer_obj
