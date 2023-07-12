from fastapi import APIRouter

from app.api.endpoints import customer, health, meta, order, product

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(customer.router, tags=["customer"])
api_router.include_router(order.router, tags=["order"])
api_router.include_router(product.router, tags=["product"])
api_router.include_router(meta.router, tags=["meta"])
