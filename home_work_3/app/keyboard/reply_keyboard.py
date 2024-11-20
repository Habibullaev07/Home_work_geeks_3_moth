from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardRemove

async def start_kb():
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(
    KeyboardButton(text="Доступные товары"),
    KeyboardButton(text="о нас"))
    return keyboard.as_markup(resize_keyboard=True, input_field_placeholder='Что вас интересует?')

del_kb = ReplyKeyboardRemove()