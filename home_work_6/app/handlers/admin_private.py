from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.enums import ParseMode

from app.database.query_db import get_users_id, get_users_all
from app.filters.chat_types import ChatTypeFilter, IsAdmin

admin_private_router = Router()
admin_private_router.message.filter(ChatTypeFilter(['private']), IsAdmin())

class Mailing(StatesGroup):
    message_text = State()

@admin_private_router.message(Command('mailing'))
async def cmd_mailing(message: Message, state: FSMContext):
    text = (
         f"<b>Привет, {message.from_user.first_name}!</b>\n\n"
        "Я рад, что ты со мной! 😊\n\n"
        "Пожалуйста, введи <i>сообщение</i> для рассылки, "
        "и я отправлю его всем пользователям. 🚀"
        )

    await message.answer(text, parse_mode=ParseMode.HTML)
    await state.set_state(Mailing.message_text)

@admin_private_router.message(Mailing.message_text)
async def mailing_message(message: Message, bot: Bot, state: FSMContext, session):
    await state.update_data(message=message.text)
    text = (
    "<b>✔️ Рассылка выполнена успешно!</b>\n"
    "Сообщение отправлено всем пользователям."
    )
    await message.answer(text, parse_mode=ParseMode.HTML)
    users = await get_users_id(session)
    data = await state.get_data()
    message_text = data['message']
    text = (
        f"<b>📢 <u>Рассылка:</u></b>\n\n"
        f"<i>{message_text}</i>\n"
        "\n<b>👉 Важное сообщение для вас!</b>"
        )
    for i in users:
       await bot.send_message(i, text, parse_mode=ParseMode.HTML)
    await state.clear()

@admin_private_router.message(Command('users'))
async def view_users(message: Message, session):
    get_users = await get_users_all(session)
    users = "<b>Список пользователей:</b>\n\n"
    for i, user in enumerate(get_users, start=1):
        users += (
            f"<b>Пользователь {i}:</b>\n"
            f" - <b>ID Telegram:</b> <code>{user.tg_id}</code>\n"
            f" - <b>ID Чата:</b> <code>{user.tg_id_chat}</code>\n"
            f" - <b>Username:</b> {user.username}\n\n"
        )
    await message.answer(users, parse_mode=ParseMode.HTML)