from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from aiogram.types import Message

from app.database.model import User

async def add_user(session: AsyncSession, message: Message):
    query_db = await session.execute (select(User).where(User.tg_id == message.from_user.id))
    user = query_db.scalar()
    if user:
        return
    else:
        add_user = User(
        tg_id=message.from_user.id,
        tg_id_chat=message.chat.id,
        username=message.from_user.username)
        session.add(add_user)
        await session.commit()
    
async def get_users_id(session: AsyncSession):
    query_db = await session.execute(select(User.tg_id))
    users = query_db.scalars().all()
    return users

async def get_users_all(session: AsyncSession):
    query_db = await session.execute(select(User))
    users = query_db.scalars().all()
    return users