from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards import  inline_kbrd, inline_kb_direction, inline_kbrd_back
from app.handlers.handlers import update_message, read_file

router3 = Router()

'''обработчики 1с программирование'''

@router3.callback_query(F.data == '1c')
async def direction_1c(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление 1С - Программирование")
    await update_message(callback, "Что именно вас интересует?", inline_kb_direction.c1prog_kb)


@router3.callback_query(F.data == 'about_direction_1c_prog')
async def about_direction_1c_prog(callback: CallbackQuery):
    await callback.answer('О направление 1c - программирование')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_1c_program.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_1c_prog)
    
    
@router3.callback_query(F.data == 'training_details_1c_prog')
async def training_details_1c_prog(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_traning_1c_program.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_1c_prog)
    
    
@router3.callback_query(F.data == 'course_cost_1c_prog')
async def course_cost_1c_prog(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_1c_program.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_1c_prog)


@router3.callback_query(F.data == 'back_direction_1c_prog')
async def back_direction_1c_prog(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', inline_kb_direction.c1prog_kb)
    
'''обработчики smm pro'''

@router3.callback_query(F.data == 'smm-pro')
async def direction_smm_pro(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление smm-pro")
    await update_message(callback, "Что именно вас интересует?", inline_kb_direction.smm_kb)


@router3.callback_query(F.data == 'about_direction_smm')
async def about_direction_smm(callback: CallbackQuery):
    await callback.answer('О направление smm-pro')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_smm_pro.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_smm)
    
    
@router3.callback_query(F.data == 'training_details_smm')
async def training_details_smm(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_traning_smm_pro.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_smm)
    
    
@router3.callback_query(F.data == 'course_cost_smm')
async def course_cost_smm(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_smm_pro.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_smm)


@router3.callback_query(F.data == 'back_direction_smm')
async def back_direction_smm(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', inline_kb_direction.smm_kb)
    
'''обработчики data science'''

@router3.callback_query(F.data == 'data_science')
async def direction_data_science(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление data_science")
    await update_message(callback, "Что именно вас интересует?",
                         inline_kb_direction.data_science_kb)


@router3.callback_query(F.data == 'about_direction_data_science')
async def about_direction_data_science(callback: CallbackQuery):
    await callback.answer('О направление data_science')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_data_science.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_data_science)
    
    
@router3.callback_query(F.data == 'training_details_data_science')
async def training_details_data_science(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_training_data_science.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_data_science)
    
    
@router3.callback_query(F.data == 'course_cost_data_science')
async def course_cost_data_science(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_data_science.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_data_science)


@router3.callback_query(F.data == 'back_direction_data_science')
async def back_direction_data_science(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', 
                         inline_kb_direction.data_science_kb)
    