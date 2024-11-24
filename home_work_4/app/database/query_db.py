from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from aiogram.types import Message 

from app.database.description_db import Register, Task, LongWords

async def orm_register(session: AsyncSession, message: Message, data):
    reg = Register(
        id_tg=message.from_user.id,
        username=data["username"],
        password=data["password"])   
    session.add(reg)
    await session.commit()
    
async def task_add(session: AsyncSession, message: Message, data):
    tasks = Task(
        id_tg=message.from_user.id,
        name_task=data['name_task'],
        description=data['description_task'])
    session.add(tasks)
    await session.commit()
    
async def check_user_login(session: AsyncSession, username, password):
    query_db = await session.execute(
        select(Register).where(Register.username == username, Register.password == password))
    check_user = query_db.scalar()
    return check_user
    
    
async def check_name(session: AsyncSession, message: Message):
    query_db = await session.execute(select(Register).where(Register.username == message.text))
    username = query_db.scalar()
    return username


async def get_tasks(session: AsyncSession):
    query_db = await session.execute(select(Task))  
    tasks = query_db.scalars().all()
    return tasks

async def clear_task(session: AsyncSession, user_id):
    await session.execute(delete(Task).filter(Task.id_tg == user_id))
    await session.commit()
    

async def get_desc_for_name(session: AsyncSession, task_id):
    query_db = await session.execute(select(Task).where(Task.id == task_id))
    description = query_db.scalar()
    return description


async def check_user_by_id(session: AsyncSession, user_id):
    query_db = await session.execute(
        select(Register).filter(Register.id_tg == user_id))
    user = query_db.scalar()
    return user


async def get_text_db(session: AsyncSession, id):
    query = await session.execute(select(LongWords.text).where(LongWords.id == id))
    long_word = query.scalar()
    return long_word