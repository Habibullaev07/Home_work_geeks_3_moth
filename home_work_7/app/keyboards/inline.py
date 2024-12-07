from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def menu_inline_kb():
    menu_kb = InlineKeyboardBuilder()
    menu_kb.add(InlineKeyboardButton(text="Отправка фото", callback_data="sending_photo"),
    InlineKeyboardButton(text="Отправка видео",callback_data="sending_video"),
    InlineKeyboardButton(text="Отправка аудиофайл", callback_data="sending_audio"))
    return menu_kb.adjust(1).as_markup()
        