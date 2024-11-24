from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardRemove

list_buttons = ["Добавить задачу", "Показать задачи", "Очистить список задач"]

async def reply_kb():
    reply_kb = ReplyKeyboardBuilder()
    for button in list_buttons:
        reply_kb.add(KeyboardButton(text=button))
    return reply_kb.adjust(2, 2).as_markup(
        resize_keyboard=True, input_field_placeholder="Что вас интересует?")
        
del_reply_kb = ReplyKeyboardRemove()

            