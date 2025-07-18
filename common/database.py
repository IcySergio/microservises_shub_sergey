from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import os

POSTGRES_USER = os.getenv("POSTGRES_USER", "app")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "pass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "app")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
DATABASE_URL = "postgresql+asyncpg://app:pass@db:5432/app"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
async_session_maker = async_session_factory