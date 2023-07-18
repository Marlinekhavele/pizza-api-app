import uuid

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.models import Product, ProductFlavour, ProductSize
from app.repositories.product_repositories import ProductRepository
from app.schemas import ProductFlavourSchema, ProductSchema, ProductSizeSchema

router = APIRouter()

# CRUD products


@router.post("/products/")
async def create_product(
    product: ProductSchema,
    product_repo: ProductRepository = Depends(ProductRepository),
):
    """
    Create a Product and store it in the database
    """
    new_product = await product_repo.create_product(product)
    return new_product


@router.get("/products")
async def get_products(db: AsyncSession = Depends(get_db_session)):
    """
    Get products all that are in the database
    """
    results = await db.execute(select(Product))
    # print(results)
    # This method retrieves all the objects from the query result set and returns them as a list.
    products = results.scalars().all()
    return products


@router.get("/products/{id}")
async def get_product_id(id: uuid.UUID, db: AsyncSession = Depends(get_db_session)):
    """
    Get products that are in the database by id
    """
    product = await db.execute(select(Product).filter(Product.id == id))
    product_obj = product.scalar_one_or_none()

    return product_obj


@router.put("/products/{id}")
async def update_product_id(
    id: uuid.UUID, product: ProductSchema, db: AsyncSession = Depends(get_db_session)
):
    """
    Update product details using their ID that is in the database
    """
    db_product = await db.execute(select(Product).filter(Product.id == id))
    product_obj = db_product.scalar_one_or_none()

    if product_obj:
        product_obj.title = product.title
        product_obj.description = product.description
        product_obj.price = product.price

        await db.commit()

    return product_obj


@router.delete("/products/{id}")
async def delete_product_id(id: uuid.UUID, db: AsyncSession = Depends(get_db_session)):
    """
    Delete product details using their UUID that is stored in the database
    """
    product = await db.execute(select(Product).filter(Product.id == id))
    product_obj = product.scalar_one_or_none()

    if product_obj:
        db.delete(product_obj)
        await db.commit()

    return product_obj


# CRUD productFlavour
@router.post("/products/flavours")
async def create_products_flavours(
    product_flavour: ProductFlavourSchema, db: AsyncSession = Depends(get_db_session)
):
    """
    Create a products flavours and store it in the database
    """
    new_product_flavour = ProductFlavour(
        id=product_flavour.id,
        active=product_flavour.active,
        product_id=product_flavour.product_id,
    )
    # print(new_product_flavour.active)
    db.add(new_product_flavour)
    await db.commit()
    await db.refresh(new_product_flavour)
    return new_product_flavour


@router.get("/products/flavours")
async def get_products_flavours(db: AsyncSession = Depends(get_db_session)):
    """
    Get all product flavours that are in the database
    """
    results = await db.execute(select(ProductFlavour))
    # print(results)
    # This method retrieves all the objects from the query result set and returns them as a list.
    product_flavours = results.scalars().all()
    return product_flavours


@router.get("/products/{id}/flavours")
async def get_products_flavours_id(
    id: uuid.UUID, db: AsyncSession = Depends(get_db_session)
):
    """
    Get products flavours  by id here
    """
    product_flavour = await db.execute(
        select(ProductFlavour).filter(ProductFlavour.id == id)
    )
    product_falvour_obj = product_flavour.scalar_one_or_none()
    return product_falvour_obj


@router.put("/products/{id}/flavours")
async def update_products_flavours_id(
    id: uuid.UUID,
    product_flavour: ProductFlavourSchema,
    db: AsyncSession = Depends(get_db_session),
):
    """
    Update products flavours details using ID's that are stored  database, here
    - we can update a field like:
    - title
    """
    db_product_flavour = await db.execute(
        select(ProductFlavour).filter(ProductFlavour.id == id)
    )
    product_flavour_obj = db_product_flavour.scalar_one_or_none()

    if product_flavour_obj:
        product_flavour_obj.title = product_flavour.title
        await db.commit()

    return product_flavour_obj


@router.delete("/products/{id}/flavours")
async def delete_products_flavours_id(
    id: uuid.UUID, db: AsyncSession = Depends(get_db_session)
):
    """
    Delete product flavour
    """
    product_flavour = await db.execute(
        select(ProductFlavour).filter(ProductFlavour.id == id)
    )
    product_flavour_obj = product_flavour.scalar_one_or_none()

    if product_flavour_obj:
        db.delete(product_flavour_obj)
        await db.commit()

    return product_flavour


# CRUD productsize
@router.post("/products/sizes")
async def create_products_sizes(
    product_size: ProductSizeSchema, db: AsyncSession = Depends(get_db_session)
):
    """
    Create a products sizes and store it in the database
    """
    new_product_size = ProductSize(
        id=product_size.id, active=product_size.active, product_id=product_size.product_id
    )
    # print(new_product_size.active)
    db.add(new_product_size)
    await db.commit()
    await db.refresh(new_product_size)
    return new_product_size


# debug
@router.get("/products/sizes")
async def get_products_size(db: AsyncSession = Depends(get_db_session)):
    """
    Get  all product sizes that are in the database
    """
    results = await db.execute(select(ProductSize))
    print(results)
    # This method retrieves all the objects from the query result set and returns them as a list.
    product_sizes = results.scalars().all()
    return product_sizes


@router.get("/products/{id}/sizes")
async def get_products_sizes_id(
    id: uuid.UUID, db: AsyncSession = Depends(get_db_session)
):
    """
    Get products sizes  by id here
    """
    product_size = await db.execute(select(ProductSize).filter(ProductSize.id == id))
    product_size_obj = product_size.scalar_one_or_none()
    return product_size_obj


@router.put("/products/{id}/sizes")
async def update_products_sizes_id(
    id: uuid.UUID,
    product_size: ProductSizeSchema,
    db: AsyncSession = Depends(get_db_session),
):
    """
    Update products sizes details using ID's that are stored  database, here
    - we can update a field like:
    - title
    """
    db_product_size = await db.execute(select(ProductSize).filter(ProductSize.id == id))
    product_size_obj = db_product_size.scalar_one_or_none()

    if product_size_obj:
        product_size_obj.title = product_size.title
        await db.commit()

    return product_size_obj


@router.delete("/products/{id}/sizes")
async def delete_products_sizes_id(
    id: uuid.UUID, db: AsyncSession = Depends(get_db_session)
):
    """
    Delete product sizes
    """
    product_size = await db.execute(select(ProductSize).filter(ProductSize.id == id))
    product_size_obj = product_size.scalar_one_or_none()

    if product_size_obj:
        db.delete(product_size_obj)
        await db.commit()
    return product_size
