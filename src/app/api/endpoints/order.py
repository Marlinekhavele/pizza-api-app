import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models import Order, OrderItem
from app.repositories.order_repositories import OrderRepository
from app.schemas import OrderItemSchema, OrderSchema

router = APIRouter()


# CRUD orders
@router.post("/orders/")
async def create_order(
    order: OrderSchema,
    order_repo: OrderRepository = Depends(OrderRepository),
):
    """
    Create a order and store it in the database
    """
    new_order = await order_repo.create_order(order)
    return new_order


@router.get("/orders/")
async def get_orders(db: AsyncSession = Depends(get_db_session)):
    """
    Get all orders that are in the database
    """
    results = await db.execute(select(Order))
    # This method retrieves all the objects from the query result set and returns them as a list.
    orders = results.scalars().all()
    return orders


@router.get("/orders/{id}")
async def get_orders_id(id: uuid.UUID, db: AsyncSession = Depends(get_db_session)):
    """
    Get orders that are in the database by id
    """
    order = await db.execute(select(Order).filter(Order.id == id))
    order_obj = order.scalar_one_or_none()
    return order_obj


@router.put("/orders/{id}")
async def update_orders_id(
    id: uuid.UUID, order: OrderSchema, db: AsyncSession = Depends(get_db_session)
):
    """
    Update order details using their ID that is in the database
    """
    db_order = await db.execute(select(Order).filter(Order.id == id))
    order_obj = db_order.scalar_one_or_none()

    if order_obj:
        order_obj.status = order.status

        await db.commit()

    return order_obj


@router.delete("/orders/{id}")
async def delete_order_id(id: uuid.UUID, db: AsyncSession = Depends(get_db_session)):
    """
    Delete order details using their UUID that is stored in the database
    """
    order = await db.execute(select(Order).filter(Order.id == id))
    order_obj = order.scalar_one_or_none()

    if order_obj:
        db.delete(order_obj)
        await db.commit()

    return order_obj


# Creating CRUD for orderitems


@router.post("/orders/items")
async def create_order_items(
    order_items: OrderItemSchema, db: AsyncSession = Depends(get_db_session)
):
    """
    create orders items
    """
    new_order_items = OrderItem(
        id=order_items.id,
        order_id=order_items.order_id,
        product_id=order_items.product_id,
        quantity=order_items.quantity,
    )
    # print(new_order_items.product_id)
    db.add(new_order_items)
    await db.commit()
    await db.refresh(new_order_items)
    return new_order_items


@router.get("/orders/{id}/items")
async def get_order_items_id(id: uuid.UUID, db: AsyncSession = Depends(get_db_session)):
    """
    Get orders items for a specific items id
    """
    order_item = await db.get(Order, id)
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    order_items = await db.execute(select(OrderItem).where(OrderItem.order_id == id))
    return order_items.scalars().all()


@router.put("/orders/{id}/items")
async def update_order_items_id(
    id: uuid.UUID, order_item: OrderItemSchema, db: AsyncSession = Depends(get_db_session)
):
    """
    Update order items for a specific order using an ID
    """
    db_order_item = await db.execute(select(OrderItem).filter(OrderItem.id == id))
    order_item_obj = db_order_item.scalar_one_or_none()

    if order_item_obj:
        order_item_obj.quantity = order_item.quantity

        await db.commit()

    return order_item_obj


@router.delete("/orders/{id}/items")
async def delete_order_items_id(
    id: uuid.UUID, db: AsyncSession = Depends(get_db_session)
):
    """
    Delete items for a specific order using an ID
    """
    order = await db.get(Order, id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order_items = await db.execute(select(OrderItem).where(OrderItem.order_id == id))
    for order_item in order_items.scalars().all():
        db.delete(order_item)
    await db.commit()
    return {"message": "Order item deleted"}
