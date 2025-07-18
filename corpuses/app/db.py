from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from common.core.config import settings

engine = create_async_engine(settings.DB_URL, future=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
