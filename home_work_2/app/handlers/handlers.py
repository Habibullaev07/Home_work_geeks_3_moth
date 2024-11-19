import asyncio

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart


from app.keyboards import reply_kbrd, inline_kbrd, inline_kbrd_back

router1 = Router()

def read_file(file_txt):
    with open(file_txt, 'r', encoding='utf-8') as file:
        return file.read()

async def update_message(callback: CallbackQuery, text, keyboard):
    await callback.message.edit_text(text, reply_markup=keyboard)
    
@router1.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать! \nВыберите что вас интересует',
                         reply_markup=reply_kbrd.reply_kb)
 
''' начинаю создание обработчиков о нас'''   

@router1.message(F.text.lower() == "о нас")
async def about_us(message: Message):
    await message.answer("Что именно вас интересует?", reply_markup=inline_kbrd.about_us_kb)


@router1.callback_query(F.data == 'about_geeks')
async def about_geeks(callback: CallbackQuery):
    await callback.answer("Вы выбрали о Geeks")
    about_us = read_file('geeks_all/about_geeks/about_us.txt')
    await update_message(callback, about_us, inline_kbrd_back.back_about_us)
    
    
@router1.callback_query(F.data == 'advantages')
async def advantages(callback: CallbackQuery):
    callback.answer('Вы выбрали наши преимущества')
    advantages_geeks = read_file('geeks_all/about_geeks/advantages.txt')
    await update_message(callback, advantages_geeks, inline_kbrd_back.back_about_us)
    
    
@router1.callback_query(F.data == "after_graduation_course")
async def after_graduation_course(callback: CallbackQuery):
    await callback.answer("Вы выбрали после окончание курсов")
    after_graduation_course_geeks = read_file('geeks_all/about_geeks/after_graduation_course.txt')
    await update_message(callback, after_graduation_course_geeks, inline_kbrd_back.back_about_us)
    

@router1.callback_query(F.data == 'back_about_us')
async def back_button(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', inline_kbrd.about_us_kb)

''' Контакты'''

@router1.message(F.text.lower() == 'контакты и локация')
async def contact(message: Message):
    await message.answer("Укажите, какой город вас интересует.",
                         reply_markup=inline_kbrd.contact_kb)

@router1.callback_query(F.data == 'bishkek')
async def bishkek(callback: CallbackQuery):
    await callback.answer('Выбрали бишкек')
    await update_message(callback, "Что вас интересует?",
                    inline_kbrd.send_bishkek_local_and_contact_kb)
    
@router1.callback_query(F.data == 'osh')
async def bishkek(callback: CallbackQuery):
    await callback.answer('Выбрали ош')
    await update_message(callback, "Что вас интересует?",
                         inline_kbrd.send_osh_local_and_contact_kb)
    
@router1.callback_query(F.data == 'kara-balta')
async def bishkek(callback: CallbackQuery):
    await callback.answer('Выбрали кара балта')
    await update_message(callback, "Что вас интересует?",
                inline_kbrd.send_kara_balta_local_and_contact_kb)
    
@router1.callback_query(F.data == 'tashkent')
async def bishkek(callback: CallbackQuery):
    await callback.answer('Выбрали Ташкент')
    await update_message(callback, "Что вас интересует?",
                    inline_kbrd.send_tashkent_local_and_contact_kb)
    

@router1.callback_query(F.data == 'send_contact_bishkek')
async def osh(callback: CallbackQuery):
    await callback.answer('Выбрали бишкек')
    await callback.message.answer_contact(phone_number="+996557052018", first_name='Geeks')
    await asyncio.sleep(1)
    
    
@router1.callback_query(F.data == 'send_contact_osh')
async def osh(callback: CallbackQuery):
    await callback.answer('Выбрали бишкек')
    await callback.message.answer_contact(phone_number="+99650052018", first_name='Geeks')
    await asyncio.sleep(1)
    

@router1.callback_query(F.data == 'send_contact_kara-balta')
async def osh(callback: CallbackQuery):
    await callback.answer('Выбрали бишкек')
    await callback.message.answer_contact(phone_number="+996777052018", first_name='Geeks')
    await asyncio.sleep(1)
    
    
@router1.callback_query(F.data == 'send_contact_tashkent')
async def osh(callback: CallbackQuery):
    await callback.answer('Выбрали бишкек')
    await callback.message.answer_contact(phone_number="+998952800101", first_name='Geeks')
    await asyncio.sleep(1)
  

@router1.callback_query(F.data == "back_contact")
async def back_contact(callback: CallbackQuery):
    await callback.answer("Назад")
    await update_message(callback, "Укажите какой город вас интересует",
                         inline_kbrd.contact_kb)