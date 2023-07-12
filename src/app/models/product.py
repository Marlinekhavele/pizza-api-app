import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..database.base import Base


class Product(Base):
    __tablename__ = "products"
    id = sa.Column(
        UUID(as_uuid=True), primary_key=True, default=sa.text("uuid_generate_v4()")
    )
    title = sa.Column(sa.String(30))
    description = sa.Column(sa.String(200))
    price = sa.Column(sa.String(30))


class ProductSize(Base):
    __tablename__ = "products_sizes"
    id = sa.Column(
        UUID(as_uuid=True), primary_key=True, default=sa.text("uuid_generate_v4()")
    )
    title = sa.Column(sa.String(30))
    active = sa.Column(sa.String(15))
    product_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey("products.id"), nullable=False, unique=True
    )
    product = relationship(Product, uselist=False, lazy="selectin")


class ProductFlavour(Base):
    __tablename__ = "products_flavours"
    id = sa.Column(
        UUID(as_uuid=True), primary_key=True, default=sa.text("uuid_generate_v4()")
    )
    title = sa.Column(sa.String(30))
    active = sa.Column(sa.String(15))
    product_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey("products.id"), nullable=False, unique=True
    )
    product = relationship(Product, uselist=False, lazy="selectin")
