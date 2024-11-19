from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards import   inline_kb_direction, inline_kbrd_back
from app.handlers.handlers import update_message, read_file

router5 = Router()

'''обработчик mobile разработчик'''

@router5.callback_query(F.data == 'mobile_developer')
async def direction_mobile(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление mobile-Разработчик")
    await update_message(callback, "Что именно вас интересует?", inline_kb_direction.mobile_kb)


@router5.callback_query(F.data == 'about_direction_mobile')
async def about_direction_mobile(callback: CallbackQuery):
    await callback.answer('О направление mobile-разработчик')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_mobile.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_mobile)
    
    
@router5.callback_query(F.data == 'training_details_mobile')
async def training_details_mobile(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_training_mobile.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_mobile)
    
    
@router5.callback_query(F.data == 'course_cost_mobile')
async def course_cost_mobile(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_mobile.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_mobile)


@router5.callback_query(F.data == 'back_direction_mobile')
async def back_direction_mobile(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', inline_kb_direction.mobile_kb)
    
'''обработчик менеджер проект'''

@router5.callback_query(F.data == 'manager_project')
async def direction_manager_project(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление Менеджер проектов")
    await update_message(callback, "Что именно вас интересует?", 
                         inline_kb_direction.manager_project_kb)


@router5.callback_query(F.data == 'about_direction_manager_project')
async def about_direction_manager_project(callback: CallbackQuery):
    await callback.answer('О направление manager_project')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_manager_project.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_manager_project)
    
    
@router5.callback_query(F.data == 'training_details_manager_project')
async def training_details_manager_project(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_training_manager_project.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_manager_project)
    
    
@router5.callback_query(F.data == 'course_cost_manager_project')
async def course_cost_manager_project(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_manager_project.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_manager_project)


@router5.callback_query(F.data == 'back_direction_manager_project')
async def back_direction_manager_project(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?',
                         inline_kb_direction.manager_project_kb)
    
'''обработчик full-stack разработчик'''

@router5.callback_query(F.data == 'fullstack')
async def direction_fullstack(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление fullstack - разработчик")
    await update_message(callback, "Что именно вас интересует?", inline_kb_direction.fullstack_kb)


@router5.callback_query(F.data == 'about_direction_fullstack')
async def about_direction_fullstack(callback: CallbackQuery):
    await callback.answer('О направление fullstack')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_fullstack.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_fullstack)
    
    
@router5.callback_query(F.data == 'training_details_fullstack')
async def training_details_fullstack(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_training_fullstack.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_fullstack)
    
    
@router5.callback_query(F.data == 'course_cost_fullstack')
async def course_cost_fullstack(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_fullstack.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_fullstack)


@router5.callback_query(F.data == 'back_direction_fullstack')
async def back_direction_fullstack(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?', inline_kb_direction.fullstack_kb)


'''программирование для детей'''

@router5.callback_query(F.data == 'programming_child')
async def direction_child_program(callback: CallbackQuery):
    await callback.answer("Вы выбрали направление Программирование для детей")
    await update_message(callback, "Что именно вас интересует?", 
                         inline_kb_direction.program_child_kb)


@router5.callback_query(F.data == 'about_direction_program_child')
async def about_direction_program_child(callback: CallbackQuery):
    await callback.answer('О направление программирование для детей')
    file_geeks = read_file('geeks_all/about_direction_geeks/about_program_child.txt')
    await update_message(callback, file_geeks, inline_kbrd_back.back_direction_program_child)
    
    
@router5.callback_query(F.data == 'training_details_program_child')
async def training_details_program_child(callback: CallbackQuery):
    await callback.answer("Подробность про обучение")
    file_traning = read_file('geeks_all/details_about_training_geeks/details_about_training_program_child.txt')
    await update_message(callback, file_traning, inline_kbrd_back.back_direction_program_child)
    
    
@router5.callback_query(F.data == 'course_cost_program_child')
async def course_cost_program_child(callback: CallbackQuery):
    await callback.answer("Стоимость курса")
    file_course_cost = read_file('geeks_all/about_curs_cost_geeks/course_cost_program_child.txt')
    await update_message(callback, file_course_cost, inline_kbrd_back.back_direction_program_child)


@router5.callback_query(F.data == 'back_direction_program_child')
async def back_direction_program_child(callback: CallbackQuery):
    await update_message(callback, 'Что именно вас интересует?',
                         inline_kb_direction.program_child_kb)
    

@router5.callback_query(F.data == 'back_direction')
async def back_direction(callback: CallbackQuery):
    await update_message(callback,"Выберите направление который вас интересует!",
                         inline_kb_direction.direction_kb)