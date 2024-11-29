import asyncio

from aiogram.types import Message
from aiogram import BaseMiddleware
from aiogram.enums import ParseMode
from typing import Callable, Dict, Any

from app.database.quary_db import get_user
from app.keyboards.reply import del_reply_kb
from app.keyboards.inline import auth_keyboard
from app.handlers.auth_users import temp_storage

class Check_user(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Any],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        session = data.get("session")
        users = await get_user(session, event.from_user.id)
        
        usernames = [user.username for user in users]
        
        if not any(username in temp_storage.values() for username in usernames):
            await event.answer("<b>⏳ Ваше время истекло.</b>", 
            parse_mode=ParseMode.HTML, reply_markup=del_reply_kb)
            await asyncio.sleep(2.5)
            await event.answer(
            "<b>🔑 Пожалуйста, войдите в свой аккаунт снова, чтобы продолжить.</b>",
            parse_mode=ParseMode.HTML, reply_markup=await auth_keyboard())
        else:
            return await handler(event, data)