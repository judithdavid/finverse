"""Add category_id to transactions

Revision ID: 9046690c46f8
Revises: 4d11220a35e5
Create Date: 2026-08-01 16:41:27.634055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9046690c46f8'
down_revision: Union[str, Sequence[str], None] = '4d11220a35e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "transactions",
        sa.Column("category_id", sa.Integer(), nullable=True),
    )

    op.create_foreign_key(
        None,
        "transactions",
        "categories",
        ["category_id"],
        ["id"],
    )

def downgrade():
    op.drop_constraint(None, "transactions", type_="foreignkey")
    op.drop_column("transactions", "category_id")
