from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.schemas.enums.product_flavour import Flavour
from app.schemas.enums.product_size import Size

from ..database.base import Base


class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="product_pk"),
        UniqueConstraint(
            "id",
            name="product_unique",
        ),
    )
    id = sa.Column(UUID(as_uuid=True), default=uuid4)
    title = sa.Column(sa.String(30))
    description = sa.Column(sa.String(200))
    price = sa.Column(sa.String(30))


class ProductSize(Base):
    __tablename__ = "products_sizes"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="product_size_pk"),
        UniqueConstraint(
            "id",
            name="product_size_unique",
        ),
    )
    id = sa.Column(UUID(as_uuid=True), default=uuid4)
    title = sa.Column(sa.Enum(Size))
    active = sa.Column(sa.String(15))
    product_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey("products.id"), nullable=False, unique=True
    )
    product = relationship(Product, uselist=False, lazy="selectin")


class ProductFlavour(Base):
    __tablename__ = "products_flavours"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="product_flavour_pk"),
        UniqueConstraint(
            "id",
            name="product_flavour_unique",
        ),
    )
    id = sa.Column(UUID(as_uuid=True), default=uuid4)
    title = sa.Column(sa.Enum(Flavour))
    active = sa.Column(sa.String(15))
    product_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey("products.id"), nullable=False, unique=True
    )
    product = relationship(Product, uselist=False, lazy="selectin")
