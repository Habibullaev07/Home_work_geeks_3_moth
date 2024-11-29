from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def auth_keyboard():
    register_kb = InlineKeyboardBuilder()
    register_kb.add(InlineKeyboardButton(text='Регистрация', callback_data='register'),
    InlineKeyboardButton(text='Авторизация', callback_data='login'))
    return register_kb.as_markup()
    
async def top_up_request_kb():
    request_top_up_kb = InlineKeyboardBuilder()
    request_top_up_kb.add(InlineKeyboardButton(text="Да", callback_data="yes_top_up"),
    InlineKeyboardButton(text='Отменить', callback_data='cancellation'))
    return request_top_up_kb.adjust(1).as_markup()

