from enum import Enum

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..database.base import Base
from .customer import Customer
from .product import Product


class Status(str, Enum):
    DRAFT = "Draft"
    PROCESSING = "Processing"
    CANCELLED = "Cancelled"
    DELIVERED = "Delivered"


class Order(Base):
    __tablename__ = "orders"
    id = sa.Column(
        UUID(as_uuid=True), primary_key=True, default=sa.text("uuid_generate_v4()")
    )
    customer_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey(Customer.id), nullable=False, unique=True
    )
    customer = relationship(Customer, uselist=False, lazy="selectin")
    status = sa.Column(sa.Enum(Status))


class OrderItem(Base):
    __tablename__ = "order_items"
    id = sa.Column(
        UUID(as_uuid=True), primary_key=True, default=sa.text("uuid_generate_v4()")
    )
    order_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey("orders.id"), nullable=False, unique=True
    )
    order = relationship(Order, uselist=False, lazy="selectin")
    product_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey("products.id"), nullable=False, unique=True
    )
    product = relationship(Product, uselist=False, lazy="selectin")
    quantity = sa.Column(sa.String(10))
