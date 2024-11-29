from aiogram.types import KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

async def menu_kb():
    list_menu = ["Просмотр баланса", "Пополнение счета", "Перевод средств", 
    "Смена пароля", "Выход из аккаунта"]
    
    menu_kb = ReplyKeyboardBuilder()
    for menu in list_menu:
        menu_kb.add(KeyboardButton(text=menu))
    return menu_kb.adjust(2).as_markup(
    resize_keyboard=True, input_field_placeholder="Что вы хотите делать?")

del_reply_kb = ReplyKeyboardRemove()
        
    