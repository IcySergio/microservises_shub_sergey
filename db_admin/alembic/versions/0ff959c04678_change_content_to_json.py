"""change content to JSON

Revision ID: 0ff959c04678
Revises: c8da10e39cb1
Create Date: 2025-07-18 02:02:11.602242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '0ff959c04678'
down_revision: Union[str, Sequence[str], None] = 'c8da10e39cb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. удалить ready, если есть
    with op.batch_alter_table("corpuses") as batch_op:
        batch_op.drop_column("ready", if_exists=True)  # type: ignore[arg-type]
    # 2. изменить type столбца content → JSONB
    op.alter_column(
        "corpuses",
        "ready",
        existing_type=sa.Boolean(),
        nullable=False,
        server_default=sa.text("false"),
    )
def downgrade() -> None:
    op.alter_column(
        "corpuses",
        "content",
        type_=sa.VARCHAR(),
        existing_type=postgresql.JSONB(),
        postgresql_using="content::text",
    )
    with op.batch_alter_table("corpuses") as batch_op:
        batch_op.add_column(sa.Column("ready", sa.Boolean(), nullable=True))