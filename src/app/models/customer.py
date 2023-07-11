import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from ..database.base import Base


class Customer(Base):
    __tablename__ = "customers"
    id = sa.Column(
        UUID(as_uuid=True), primary_key=True, default=sa.text("uuid_generate_v4()")
    )
    name = sa.Column(sa.String(30))
    phone = sa.Column(sa.String(25))
    email = sa.Column(sa.String(254))
