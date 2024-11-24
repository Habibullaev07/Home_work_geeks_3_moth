import os 
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database.description_db import Base


connect = create_async_engine(os.getenv('DATABASE'), echo=True)

session_maker = async_sessionmaker(bind=connect, class_=AsyncSession, expire_on_commit=False)

async def create_db():
    async with connect.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        
        
async def drop_db():
    async with connect.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        