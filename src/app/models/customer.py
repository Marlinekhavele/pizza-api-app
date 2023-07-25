from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from ..database.base import Base


class Customer(Base):
    __tablename__ = "customers"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="customer_pk"),
        UniqueConstraint(
            "id",
            name="customer_unique",
        ),
    )
    id = sa.Column(UUID(as_uuid=True), default=uuid4)
    name = sa.Column(sa.String(30))
    phone = sa.Column(sa.String(25))
    email = sa.Column(sa.String(254))
