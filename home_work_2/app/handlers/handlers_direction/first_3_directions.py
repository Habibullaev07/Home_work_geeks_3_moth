from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.keyboards import  inline_kb_direction, inline_kbrd_back
from app.handlers.handlers import update_message, read_file

router2 = Router()

@router2.message(F.text.lower() == 'направления')
async def direction_geeks(message: Message):
    await message.answer("Выберите направление который вас интересует!",
                         reply_markup=inline_kb_direction.direction_kb)


@router2.callback_query(F.data == 'backend')
async def direction_backend(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление backend")
    await update_message(callback, "Что именно вас интересует?", inline_kb_direction.backend_kb)


@router2.callback_query(F.data == 'about_direction_backend')
async def about_direction_backend(callback: CallbackQuery):
    await callback.answer('О направление Backend')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_backend.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_backend)
    
    
@router2.callback_query(F.data == 'training_details_backend')
async def training_details_backend(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_traning_backend.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_backend)
    
    
@router2.callback_query(F.data == 'course_cost_backend')
async def course_cost_backend(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_backend.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_backend)


@router2.callback_query(F.data == 'back_direction_backend')
async def back_button_backend(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', inline_kb_direction.backend_kb)

'''Обработчики для направление frontend'''


@router2.callback_query(F.data == 'frontend')
async def direction_frontend(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление frontend")
    await update_message(callback, "Что именно вас интересует?", inline_kb_direction.frontend_kb)


@router2.callback_query(F.data == 'about_direction_frontend')
async def about_direction_frontend(callback: CallbackQuery):
    await callback.answer('О направление Frontend')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_frontend.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_frontend)
    
    
@router2.callback_query(F.data == 'training_details_frontend')
async def training_details_frontend(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_traning_frontend.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_frontend)
    
    
@router2.callback_query(F.data == 'course_cost_frontend')
async def course_cost_frontend(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_frontend.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_frontend)


@router2.callback_query(F.data == 'back_direction_frontend')
async def back_button_backend(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', inline_kb_direction.frontend_kb)
    
    
'''Обработчики для ux/ui дизайнер'''

@router2.callback_query(F.data == 'ux')
async def direction_ux(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление UX/UI - дизайнер")
    await update_message(callback, "Что именно вас интересует?", inline_kb_direction.ux_kb)


@router2.callback_query(F.data == 'about_direction_ux')
async def about_direction_ux(callback: CallbackQuery):
    await callback.answer('О направление ux/ui - дизайнер')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_ux.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_ux)
    
    
@router2.callback_query(F.data == 'training_details_ux')
async def training_details_ux(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_traning_ux.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_ux)
    
    
@router2.callback_query(F.data == 'course_cost_ux')
async def course_cost_ux(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_ux.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_ux)


@router2.callback_query(F.data == 'back_direction_ux')
async def back_direction_ux(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', inline_kb_direction.ux_kb)