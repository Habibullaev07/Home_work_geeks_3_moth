from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Направления'),
        KeyboardButton(text='Контакты и Локация'),
    ],
    [
        KeyboardButton(text="О нас")
    ],
], resize_keyboard=True, input_field_placeholder="Выберите что вас интересует")