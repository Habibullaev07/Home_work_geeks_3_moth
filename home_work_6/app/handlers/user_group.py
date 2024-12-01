from aiogram.types import Message
from aiogram import Bot, Router
from aiogram.filters import Command, CommandStart
from aiogram.enums import ParseMode

from app.filters.chat_types import ChatTypeFilter
from app.database.query_db import add_user

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))

@user_group_router.message(CommandStart())
async def cmd_start(message: Message, session):
    await add_user(session, message)
    text = (
        f"<b>Привет, {message.from_user.first_name}!</b>\n"
        "Добро пожаловать в нашу беседу. Рады вас видеть!"
    )
    await message.answer(text, parse_mode=ParseMode.HTML)
    
    
@user_group_router.message(Command('admin'))
async def get_admins(message: Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    admins_list = [
        user.user.id 
        for user in admins_list if user.status == "creator" or user.status == "administrator"]   
    
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list and bot.id in admins_list:
        await message.delete()
    