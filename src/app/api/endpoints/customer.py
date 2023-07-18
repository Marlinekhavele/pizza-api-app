import uuid

from fastapi import APIRouter, Depends

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
async def get_customer_id(id: uuid.UUID, repo: CustomerRepository = Depends(CustomerRepository)):
    """
    Get customers that are in the database by id
    """
    return await repo.get_customer_by_id(id)


@router.put("/customers/{id}")
async def update_customer_id(
    id: uuid.UUID,
    customer: CustomerSchema,
    repo: CustomerRepository = Depends(CustomerRepository),
):
    """
    Update customer details using their ID that is in the database
    """
    updated_customer = await repo.update_customer(
        id, customer.name, customer.email, customer.phone
    )
    return updated_customer


@router.delete("/customers/{id}")
async def delete_customer_id(
    id: uuid.UUID, repo: CustomerRepository = Depends(CustomerRepository)
):
    """
    Delete customer details using their UUID that is stored in the database
    """
    deleted_customer = await repo.delete_customer(id)
    return deleted_customer
