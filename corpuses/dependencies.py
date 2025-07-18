from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.database import async_session_factory

async def get_session() -> AsyncSession:  # noqa: D103
    async with async_session_factory() as session:
        yield session
