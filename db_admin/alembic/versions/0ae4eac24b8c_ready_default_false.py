"""ready default false

Revision ID: 0ae4eac24b8c
Revises: 0ff959c04678
Create Date: 2025-07-18 18:20:20.331488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ae4eac24b8c'
down_revision: Union[str, Sequence[str], None] = '0ff959c04678'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # если вдруг оказались NULL‑ы – сначала обнуляем
    op.execute("UPDATE corpuses SET ready = false WHERE ready IS NULL")

    op.alter_column(
        "corpuses",
        "ready",
        existing_type=sa.Boolean(),
        nullable=False,
        server_default=sa.text("false"),   # ← дефолт
    )


def downgrade() -> None:
    op.alter_column(
        "corpuses",
        "ready",
        existing_type=sa.Boolean(),
        nullable=False,
        server_default=None,               # ← откат
    )
