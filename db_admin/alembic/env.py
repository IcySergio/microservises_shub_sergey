from __future__ import annotations

import os

from alembic import context
from sqlalchemy import pool

from pathlib import Path
import sys

HERE = Path(__file__).resolve()
for p in [HERE, *HERE.parents]:
    if (p / "common").is_dir():
        sys.path.append(str(p))
        break
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from common import Base
import common.models
target_metadata = Base.metadata

from common.core.config import settings
config = context.config
target_metadata = Base.metadata


def get_url() -> str:
    """
    Returns sync SQLAlchemy URL for migrations.
    Priority: env → settings.
    """
    return os.getenv("SYNC_DB_URL", settings.SYNC_DB_URL)


def run_migrations_offline() -> None:
    url = get_url()
    context.configure(  # type: ignore[attr-defined]
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():  # type: ignore[attr-defined]
        context.run_migrations()  # type: ignore[attr-defined]


def run_migrations_online() -> None:
    from sqlalchemy import create_engine
    connectable = create_engine(get_url(), poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(  # type: ignore[attr-defined]
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():  # type: ignore[attr-defined]
            context.run_migrations()  # type: ignore[attr-defined]



if context.is_offline_mode():  # type: ignore[attr-defined]
    run_migrations_offline()
else:
    run_migrations_online()
