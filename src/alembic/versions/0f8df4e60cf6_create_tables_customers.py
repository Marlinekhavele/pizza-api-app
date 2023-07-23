"""create tables customers

Revision ID: 0f8df4e60cf6
Revises:
Create Date: 2023-07-23 23:31:22.065589

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0f8df4e60cf6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "customers",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(length=30), nullable=True),
        sa.Column("phone", sa.String(length=25), nullable=True),
        sa.Column("email", sa.String(length=254), nullable=True),
        sa.PrimaryKeyConstraint("id", name="customer_pk"),
        sa.UniqueConstraint("id", name="customer_unique"),
    )
    op.create_table(
        "products",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(length=30), nullable=True),
        sa.Column("description", sa.String(length=200), nullable=True),
        sa.Column("price", sa.String(length=30), nullable=True),
        sa.PrimaryKeyConstraint("id", name="product_pk"),
        sa.UniqueConstraint("id", name="product_unique"),
    )
    op.create_table(
        "orders",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("customer_id", sa.UUID(), nullable=False),
        sa.Column(
            "status",
            sa.Enum("DRAFT", "PROCESSING", "CANCELLED", "DELIVERED", name="orderstatus"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["customer_id"],
            ["customers.id"],
        ),
        sa.PrimaryKeyConstraint("id", name="order_pk"),
        sa.UniqueConstraint("customer_id"),
        sa.UniqueConstraint("id", name="order_unique"),
    )
    op.create_table(
        "products_flavours",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "title",
            sa.Enum("MAGARITTA", "HAWAIIAN", "BBQSTEAK", "PEPORONI", name="flavour"),
            nullable=True,
        ),
        sa.Column("active", sa.String(length=15), nullable=True),
        sa.Column("product_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.PrimaryKeyConstraint("id", name="product_flavour_pk"),
        sa.UniqueConstraint("id", name="product_flavour_unique"),
        sa.UniqueConstraint("product_id"),
    )
    op.create_table(
        "products_sizes",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "title", sa.Enum("LARGE", "MEDIUM", "SMALL", name="size"), nullable=True
        ),
        sa.Column("active", sa.String(length=15), nullable=True),
        sa.Column("product_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.PrimaryKeyConstraint("id", name="product_size_pk"),
        sa.UniqueConstraint("id", name="product_size_unique"),
        sa.UniqueConstraint("product_id"),
    )
    op.create_table(
        "order_items",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("order_id", sa.UUID(), nullable=False),
        sa.Column("product_id", sa.UUID(), nullable=False),
        sa.Column("quantity", sa.String(length=10), nullable=True),
        sa.ForeignKeyConstraint(
            ["order_id"],
            ["orders.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.PrimaryKeyConstraint("id", name="order_item_pk"),
        sa.UniqueConstraint("id", name="order_item_unique"),
        sa.UniqueConstraint("order_id"),
        sa.UniqueConstraint("product_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("order_items")
    op.drop_table("products_sizes")
    op.drop_table("products_flavours")
    op.drop_table("orders")
    op.drop_table("products")
    op.drop_table("customers")
    # ### end Alembic commands ###
