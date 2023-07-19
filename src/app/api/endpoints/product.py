import uuid

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db_session
from app.repositories.product_repositories import ProductRepository
from app.repositories.product_flavour_repositories import ProductFlavourRepository
from app.repositories.product_size_repositories import ProductSizeRepository
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
async def get_products(repo:ProductRepository = Depends(ProductRepository)):
    """
    Get all products on the data
    """
    return await repo.get_products()


@router.get("/products/{id}")
async def get_product_id(id: uuid.UUID, repo: ProductRepository = Depends(ProductRepository)):
    """
    Get products that are in the database by id
    """
    return await repo.get_product_by_id(id)
 

@router.put("/products/{id}")
async def update_product_id(
    id: uuid.UUID, product_obj:ProductSchema,repo: ProductRepository = Depends(ProductRepository)
):
    """
    Update product details using their ID that is in the database
    """
    updated_product = await repo.update_product(
        id,  
        product_obj.title,
        product_obj.description,
        product_obj.price 
    )
    return updated_product

@router.delete("/products/{id}")
async def delete_product_id(
    id: uuid.UUID, repo: ProductRepository = Depends(ProductRepository)
):
    """
    Delete product details using their UUID that is stored in the database
    """
    deleted_product = await repo.delete_product(id)
    return deleted_product


# CRUD productFlavour
@router.post("/products/flavours/")
async def create_product_flavours(
    product_flavour: ProductFlavourSchema,
    product_flavour_repo: ProductFlavourRepository = Depends(ProductFlavourRepository),
):
    """
    Create a Product Flavour and store it in the database
    """
    new_product_flavour = await product_flavour_repo.create_product_flavours(product_flavour)
    return new_product_flavour

@router.get("/products/flavours/")
async def get_products_flavours(product_flavour_repo: ProductFlavourRepository = Depends(ProductFlavourRepository)):
    """
    Get all product flavours that are in the database
    """
    return await product_flavour_repo.get_products_flavours()


@router.get("/products/{id}/flavours")
async def get_products_flavours_id(
    id: uuid.UUID, product_flavour_repo: ProductFlavourRepository = Depends(ProductFlavourRepository)
):
    """
    Get products flavours  by id here
    """
    return await product_flavour_repo.get_product_flavour_by_id(id)
 


@router.put("/products/{id}/flavours")
async def update_products_flavours_id(
    id: uuid.UUID,
    product_flavour: ProductFlavourSchema,
    repo: ProductFlavourRepository = Depends(ProductFlavourRepository),
):
    """
    Update products flavours details using ID's that are stored  database, here
    - we can update a field like:
    - title
    """
    updated_product_flavour = await repo.update_product_flavour(
        id,
        product_flavour.title
    )
    return updated_product_flavour


@router.delete("/products/{id}/flavours")
async def delete_products_flavours_id(
    id: uuid.UUID, repo: ProductFlavourRepository = Depends(ProductFlavourRepository)
):
    """
    Delete product flavour using their UUID that is stored in the database
    """
    delete_product_flavour = await repo.delete_product_flavour(id)
    return delete_product_flavour


# CRUD productsize
@router.post("/products/sizes")
async def create_products_sizes(
    product_size: ProductSizeSchema, product_size_repo: ProductSizeRepository = Depends(ProductSizeRepository),
):
    """
    Create a products sizes and store it in the database
    """
    new_product_size = await product_size_repo.create_product_flavours(product_size)
    return new_product_size


@router.get("/products/sizes")
async def get_products_size(product_size_repo: ProductSizeRepository = Depends(ProductSizeRepository)):
    """
    Get  all product sizes that are in the database
    """
    return await product_size_repo.get_products_sizes()



@router.get("/products/{id}/sizes")
async def get_products_sizes_id(
    id: uuid.UUID, product_size_repo: ProductSizeRepository = Depends(ProductSizeRepository)
):
    """
    Get products sizes  by id here
    """
    return await product_size_repo.get_product_size_by_id(id)

  


@router.put("/products/{id}/sizes")
async def update_products_sizes_id(
    id: uuid.UUID,
    product_size: ProductSizeSchema,
        repo: ProductSizeRepository = Depends(ProductSizeRepository),
):
    """
    Update products sizes details using ID's that are stored  database, here
    - we can update a field like:
    - title
    """
    updated_product_size = await repo.update_product_size(
        id,
        product_size.title
    )
    return updated_product_size



@router.delete("/products/{id}/sizes")
async def delete_products_sizes_id(
    id: uuid.UUID,repo: ProductSizeRepository = Depends(ProductSizeRepository)
):
    """
    Delete product sizes
    """
    delete_product_size = await repo.delete_product_size(id)
    return delete_product_size
    
