import uuid

from fastapi import APIRouter, Depends, HTTPException

from app.repositories.order_repositories import OrderRepository
from app.repositories.order_item_repositories import OrderItemRepository
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
async def get_orders(order_repo: OrderRepository = Depends(OrderRepository),
):
    """
    Get all orders that are in the database
    """
    return await order_repo.get_orders()

    

@router.get("/orders/{id}")
async def get_orders_id(id: uuid.UUID, order_repo: OrderRepository = Depends(OrderRepository)):
    """
    Get orders that are in the database by id
    """
    return await order_repo.get_order_by_id(id)



@router.put("/orders/{id}")
async def update_orders_id(
    id: uuid.UUID, order: OrderSchema, order_repo: OrderRepository = Depends(OrderRepository)
):
    """
    Update order details using their ID that is in the database
    """
    updated_order = await order_repo.update_order_id(
        id,
        order.status
    )
    return updated_order
   

@router.delete("/orders/{id}")
async def delete_order_id(id: uuid.UUID, order_repo: OrderRepository = Depends(OrderRepository)):
    """
    Delete order details using their UUID that is stored in the database
    """
    delete_order = await order_repo.delete_order(id)
    return delete_order
   


# Creating CRUD for orderitems


@router.post("/orders/items")
async def create_order_items(
    order_items: OrderItemSchema, repository: OrderItemRepository = Depends(OrderItemRepository),

):
    """
    create orders items
    """
    new_order_item = await repository.create_order_items(order_items)
    return new_order_item

@router.get("/orders/items")
async def get_order_items(order_repo: OrderItemRepository = Depends(OrderItemRepository),
):
    """
    Get all orders items that are in the database
    """
    return await order_repo.get_orders_items()


@router.get("/orders/{id}/items")
async def get_order_items_id(id: uuid.UUID, repository: OrderItemRepository = Depends(OrderItemRepository)):
    """
    Get orders items for a specific items id
    """
    order_items = await repository.get_order_items_by_id(id)
    if not order_items:
        raise HTTPException(status_code=404, detail="Order item not found")

    return order_items
    
@router.put("/orders/{id}/items")
async def update_order_items_id(
    id: uuid.UUID,
    order_item: OrderItemSchema,
    order_item_repository: OrderItemRepository = Depends(OrderItemRepository),
):
    """
    Update order items for a specific order using an ID
    """
    db_order_item = await order_item_repository.get_order_items_by_id(id)
    if not db_order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    updated_order_item = await order_item_repository.update_order_items_id(id, order_item.quantity)

    return updated_order_item


@router.delete("/orders/{id}/items")
async def delete_order_items_id(
    id: uuid.UUID,
    order_item_repository: OrderItemRepository = Depends(OrderItemRepository),
):
    """
    Delete items for a specific order using an ID
    """
    order = await order_item_repository.get_order_items_by_id(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    await order_item_repository.delete_order_items_id(id)

    return {"message": "Order item deleted"}
