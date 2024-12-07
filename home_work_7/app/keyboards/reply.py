from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

async def reply_menu_kb():
    menu_kb = ReplyKeyboardBuilder()
    menu_kb.add(KeyboardButton(text="Отправка сообщение"),
                KeyboardButton(text="Отправка различных файлов"))
    return menu_kb.adjust(1).as_markup(
    resize_keyboard=True, input_field_placeholder="Что вы хотите делать?")
