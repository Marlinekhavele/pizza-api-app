import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.schemas.enums.order import OrderStatus

from ..database.base import Base
from .customer import Customer
from .product import Product
from sqlalchemy import (
    PrimaryKeyConstraint,
    UniqueConstraint,
)


class Order(Base):
    __tablename__ = "orders"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="order_pk"),
        UniqueConstraint(
            "id",
            name="order_unique",
        ),
    )
    id = sa.Column(UUID(as_uuid=True), default=uuid4)
    customer_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey(Customer.id), nullable=False, unique=True
    )
    customer = relationship(Customer, uselist=False, lazy="selectin")
    status = sa.Column(sa.Enum(OrderStatus))



class OrderItem(Base):
    __tablename__ = "order_items"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="order_item_pk"),
        UniqueConstraint(
            "id",
            name="order_item_unique",
        ),
    )
    id = sa.Column(UUID(as_uuid=True), default=uuid4)
    order_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey("orders.id"), nullable=False, unique=True
    )
    order = relationship(Order, uselist=False, lazy="selectin")
    product_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey("products.id"), nullable=False, unique=True
    )
    product = relationship(Product, uselist=False, lazy="selectin")
    quantity = sa.Column(sa.String(10))
