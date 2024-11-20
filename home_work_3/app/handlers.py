import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from app.keyboard.inline_keyboard import *
from app.keyboard.reply_keyboard import start_kb, del_kb

router = Router()

def read_file(txt):
    with open(txt, 'r', encoding='utf-8') as file_txt:
        return file_txt.read()
    

@router.message(CommandStart())
async def cmd_start(message: Message):
    start_txt = read_file('text_for_magazine/for_command_start.txt')
    await message.answer(start_txt, reply_markup=await start_kb())
    
    
@router.message(F.text.lower() == "доступные товары")
async def available_products(message: Message):
    await message.answer('Доступные товары!', reply_markup=await available_products_kb())
    
    
@router.callback_query(F.data == 'safety_glass')
async def safely_glass(callback: CallbackQuery):
    await callback.answer("Выбрано защитные стекла")
    await callback.message.answer("Доступные защитные стекла для смартфонов",
                                  reply_markup=await kb_for_safety_glass())


@router.callback_query(F.data == 'samsung')
async def samsung(callback: CallbackQuery):
    await callback.answer("Выбрано samsung")
    await callback.message.answer("Доступные защитные стекла", 
                            reply_markup=await samsung_safety_glass_kb())
    
@router.callback_query(F.data == 'galaxy_s23')
async def galaxy_s23(callback: CallbackQuery):
    await callback.answer('Выбрано galaxy_s23')
    galaxy_s23 = read_file('text_for_magazine/galaxy_s23.txt')
    await callback.message.answer(galaxy_s23)
    await asyncio.sleep(1)
    registration = read_file('text_for_magazine/galaxy_s23_yes.txt')
    await callback. message.answer(registration, reply_markup=await registration_kb())
    
@router.callback_query(F.data == 'galaxy_s23+')
async def galaxy_s23(callback: CallbackQuery):
    await callback.answer('Выбрано galaxy_s23+')
    galaxy_s23 = read_file('text_for_magazine/galaxy_s23+.txt')
    await callback.message.answer(galaxy_s23)
    await asyncio.sleep(1)
    registration = read_file('text_for_magazine/galaxy_s23+_yes.txt')
    await callback. message.answer(registration, reply_markup=await registration_kb())
    
@router.callback_query(F.data == 'galaxy_s23_ultra')
async def galaxy_s23(callback: CallbackQuery):
    await callback.answer('Выбрано galaxy_s23 ultra')
    galaxy_s23 = read_file('text_for_magazine/galaxy_s23_ultra.txt')
    await callback.message.answer(galaxy_s23)
    await asyncio.sleep(1)
    registration = read_file('text_for_magazine/galaxy_s23_ultra_yes.txt')
    await callback. message.answer(registration, reply_markup=await registration_kb())
    
@router.callback_query(F.data == 'registration')
async def registration(callback: CallbackQuery):
    await callback.answer("Оформление заказа")
    registration = read_file('text_for_magazine/registration.txt')
    await callback.message.answer(registration, reply_markup=del_kb)

@router.callback_query(F.data == 'cancellation')
async def cancellation(callback: CallbackQuery):
    await callback.answer("Отмена")
    cancel = read_file('text_for_magazine/cancellation.txt')
    await callback.message.answer(cancel)

@router.message(F.text.lower() == 'о нас')
async def about_us(message: Message):
    about_us = read_file('text_for_magazine/about_us.txt')
    await message.answer(about_us)
    