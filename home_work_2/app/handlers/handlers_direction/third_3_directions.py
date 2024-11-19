from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards import  inline_kb_direction, inline_kbrd_back
from app.handlers.handlers import update_message, read_file

router4 = Router()

'''обработчики graphics design'''

@router4.callback_query(F.data == 'graphic_design')
async def direction_graphic_design(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление Graphic-Design")
    await update_message(callback, "Что именно вас интересует?",
                         inline_kb_direction.graphic_design_kb)


@router4.callback_query(F.data == 'about_direction_graphic_design')
async def about_direction_graphic_design(callback: CallbackQuery):
    await callback.answer('О направление graphic-design')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_graphic_design.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_graphic_design)
    
    
@router4.callback_query(F.data == 'training_details_graphic_design')
async def training_details_graphic_design(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_training_graphic_design.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_graphic_design)
    
    
@router4.callback_query(F.data == 'course_cost_graphic_design')
async def course_cost_graphic_design(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_graphic_design.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_graphic_design)


@router4.callback_query(F.data == 'back_direction_graphic_design')
async def back_direction_graphic_design(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?',
                         inline_kb_direction.graphic_design_kb)

'''обработчики тестировщик по '''

@router4.callback_query(F.data == 'test_po')
async def direction_test_po(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление Тестировщик-ПО")
    await update_message(callback, "Что именно вас интересует?", inline_kb_direction.test_po_kb)


@router4.callback_query(F.data == 'about_direction_test_po')
async def about_direction_test_po(callback: CallbackQuery):
    await callback.answer('О направление test_по')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_test_po.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_test_po)
    
    
@router4.callback_query(F.data == 'training_details_test_po')
async def training_details_test_po(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_training_test_po.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_test_po)
    
    
@router4.callback_query(F.data == 'course_cost_test_po')
async def course_cost_test_po(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_test_po.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_test_po)


@router4.callback_query(F.data == 'back_direction_test_po')
async def back_direction_test_po(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', inline_kb_direction.test_po_kb)
    
'''обработчики основы программирование'''

@router4.callback_query(F.data == 'basic-program')
async def direction_basic_program(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление Основы программирование ")
    await update_message(callback, "Что именно вас интересует?",
                         inline_kb_direction.basic_program_kb)


@router4.callback_query(F.data == 'about_direction_basic_program')
async def about_direction_basic_program(callback: CallbackQuery):
    await callback.answer('О направление Основы программирование')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_basic_program.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_basic_program)
    
    
@router4.callback_query(F.data == 'training_details_basic_program')
async def training_details_basic_program(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_training_basic_program.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_basic_program)
    
    
@router4.callback_query(F.data == 'course_cost_basic_program')
async def course_cost_basic_program(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_basic_program.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_basic_program)


@router4.callback_query(F.data == 'back_direction_basic_program')
async def back_direction_basic_program(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', 
                         inline_kb_direction.basic_program_kb)