from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from aiogram.types import Message

from app.database.model import User, Text_for_handlers

async def register_user_db(session: AsyncSession, message: Message, data):
    register_user = User(
        tg_id=message.from_user.id,
        name=data['name'],
        username=data['username'],
        password=data['password'])
    session.add(register_user)
    await session.commit()

async def get_username(session: AsyncSession, message: str):
    quary_db = await session.execute(select(User).where(User.username == message))
    username = quary_db.scalar()
    return username

async def update_password(session: AsyncSession, username: str, new_password: str):
    quary_db = update(User).where(User.username == username).values(password=new_password)
    await session.execute(quary_db)
    await session.commit()

async def get_text_from_db(session: AsyncSession, id: int):
    query_db = await session.execute(select(Text_for_handlers.text).where(Text_for_handlers.id == id))
    text_for_handlers = query_db.scalar()
    return text_for_handlers

async def get_user(session: AsyncSession, tg_id):
    query_db = await session.execute(select(User).where(User.tg_id == tg_id))
    user = query_db.scalars().all()
    return  user 