import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database.model import Base

engine = create_async_engine(os.getenv('DATABASE'), echo=True)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def clear_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)