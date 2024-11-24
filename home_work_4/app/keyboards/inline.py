from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.query_db import get_tasks

async def login_kb():
    login_kb = InlineKeyboardBuilder()
    login_kb.add(InlineKeyboardButton(text="Регистрация", callback_data='register'),
                 InlineKeyboardButton(text="Авторизация", callback_data='login'))
    
    return login_kb.adjust(1, 1).as_markup()


async def show_tasks(session):
    tasks = await get_tasks(session)
    if not tasks:
        return None
    
    show_task_kb = InlineKeyboardBuilder()
    for task in tasks:
        show_task_kb.add(InlineKeyboardButton(text=task.name_task, callback_data=f"task_{task.id}"))
    return show_task_kb.adjust(1).as_markup()


