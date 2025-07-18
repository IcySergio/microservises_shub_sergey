from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from common.core.config import settings  # ваш pydantic‑config

engine = create_async_engine(settings.ASYNC_DB_URL, future=True, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
