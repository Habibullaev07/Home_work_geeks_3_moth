import os 

from aiogram import  Router
from aiogram.types import Message
from aiogram.filters import  CommandStart
from aiogram.enums import ParseMode

from app.filters.chat_types import ChatTypeFilter
from app.database.query_db import add_user

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter('private'))

@user_private_router.message(CommandStart())
async def cmd_start(message: Message, session, bot):
    member = await bot.get_chat_member(chat_id=os.getenv('GROUP_CHAT_ID'), 
                                       user_id=message.from_user.id)
    if member.status in ["member", "administrator", "creator"]:
        text = (
        f"<b>Привет, {message.from_user.first_name}!</b>\n"
        "Если у вас есть вопросы, касающиеся группы, "
        "напишите нашему владельцу группы: <a href='https://t.me/Habibullaev_07'>@Habibullaev_07</a>"
        )
        await message.answer(text, parse_mode=ParseMode.HTML)

    else:
        text = (
        "<b>Привет!</b>\n"
        "Я создан для работы с группой. Если хотите вступить в группу, "
        "напишите нашему владельцу группы: <a href='https://t.me/Habibullaev_07'>@Habibullaev_07</a>"
        )
        await message.answer(text, parse_mode=ParseMode.HTML)

