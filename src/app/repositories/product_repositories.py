# will handle all my product logic 
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import  Depends

from app.models import Product
from app.deps import get_db_session
class ProductRepository:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def create_product(self, product_data):
        new_product = Product(
            id=product_data.id,
              title=product_data.title,
        description=product_data.description,
        price=product_data.price,
        )
        self.db.add(new_product)
        await self.db.commit()
        await self.db.refresh(new_product)
        return new_product
