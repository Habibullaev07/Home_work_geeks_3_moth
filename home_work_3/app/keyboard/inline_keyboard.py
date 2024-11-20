from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

async def available_products_kb():
    products_kb = InlineKeyboardBuilder()
    products_kb.add(InlineKeyboardButton(text="Защитные стекла", callback_data='safety_glass'))
    return products_kb.as_markup()
    
async def kb_for_safety_glass():
    safety_glass_kb = InlineKeyboardBuilder()
    safety_glass_kb.add(InlineKeyboardButton(text="Samsung", callback_data='samsung'))
    return safety_glass_kb.as_markup()

async def samsung_safety_glass_kb():
    samsung_kb = InlineKeyboardBuilder()
    samsung_kb.add(InlineKeyboardButton(text="Galaxy S23", callback_data='galaxy_s23'),
                   InlineKeyboardButton(text="Galaxy S23+", callback_data='galaxy_s23+'),
                   InlineKeyboardButton(text="Galaxy S23 Ultra", callback_data='galaxy_s23_ultra'))
    return samsung_kb.adjust(2, 2).as_markup()
    
async def registration_kb():
    registration_kb = InlineKeyboardBuilder()
    registration_kb.add(InlineKeyboardButton(text='✅ Да, оформить заказ', callback_data='registration'),
                        InlineKeyboardButton(text='❌ Отмена', callback_data='cancellation'))
    
    return registration_kb.adjust(1,1).as_markup()
        
    
    