from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any
from app.database.query_db import check_user_by_id

from app.keyboards.inline import login_kb



class CheckRegister(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Any],
        event:  Message,
        data: Dict[str, Any],
    ) -> Any:
        user_id = None
        if isinstance(event, Message):
            user_id = event.from_user.id
            
        session = data.get("session")
        user  = await check_user_by_id(session, user_id)
        if user:
            return await handler(event, data)
        else:
            await event.answer("Пожалуйста: \nЗарегистрируйтесь для взаимодействия",
                               reply_markup=await login_kb())
            return
        