from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

direction_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Backend-разработчик', callback_data='backend'),
        InlineKeyboardButton(text='Frontend-разработчик', callback_data='frontend'),
        InlineKeyboardButton(text='UX/UI-дизайнер', callback_data='ux'),
    ],
    [
        InlineKeyboardButton(text='1С программирование', callback_data='1c'),
        InlineKeyboardButton(text='SMM PRO', callback_data='smm-pro'),
        InlineKeyboardButton(text='Data science & machine learning', callback_data='data_science'), 
    ],
    [
        InlineKeyboardButton(text='Graphic design and motion', callback_data='graphic_design'),
        InlineKeyboardButton(text='Тестировщик ПО', callback_data='test_po'),
        InlineKeyboardButton(text='Основы программирования', callback_data='basic-program'),
       
    ],
    [
        InlineKeyboardButton(text='Mobile-разработчик', callback_data='mobile_developer'),
        InlineKeyboardButton(text='Менеджер проектов', callback_data='manager_project'),
        InlineKeyboardButton(text='Fullstack-разработчик', callback_data='fullstack'),
    ],
    [
        InlineKeyboardButton(text='Программирование для детей', callback_data='programming_child'),
    ]])


backend_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Backend", callback_data='about_direction_backend')],
    [InlineKeyboardButton(text="Подробность про обучение",callback_data='training_details_backend')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_backend')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

frontend_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Frontend", callback_data='about_direction_frontend')],
    [InlineKeyboardButton(text="Подробность про обучение", callback_data='training_details_frontend')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_frontend')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

ux_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении UX/UI - дизайнер", callback_data='about_direction_ux')],
    [InlineKeyboardButton(text="Подробность про обучение", callback_data='training_details_ux')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_ux')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

c1prog_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении 1C - Программирование", 
                          callback_data='about_direction_1c_prog')],
    [InlineKeyboardButton(text="Подробность про обучение", 
                          callback_data='training_details_1c_prog')],
    [InlineKeyboardButton(text="Стоимость обучение", 
                          callback_data='course_cost_1c_prog')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

smm_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении SMM PRO", 
                          callback_data='about_direction_smm')],
    [InlineKeyboardButton(text="Подробность про обучение",
                          callback_data='training_details_smm')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_smm')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

data_science_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Data science...", 
                          callback_data='about_direction_data_science')],
    [InlineKeyboardButton(text="Подробность про обучение", 
                          callback_data='training_details_data_science')],
    [InlineKeyboardButton(text="Стоимость обучение", 
                          callback_data='course_cost_data_science')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

graphic_design_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Graphic_design...", 
                          callback_data='about_direction_graphic_design')],
    [InlineKeyboardButton(text="Подробность про обучение", 
                          callback_data='training_details_graphic_design')],
    [InlineKeyboardButton(text="Стоимость обучение", 
                          callback_data='course_cost_graphic_design')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

test_po_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Тестировщик ПО", 
                          callback_data='about_direction_test_po')],
    [InlineKeyboardButton(text="Подробность про обучение", 
                          callback_data='training_details_test_po')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_test_po')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

basic_program_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Основы программирование", 
                          callback_data='about_direction_basic_program')],
    [InlineKeyboardButton(text="Подробность про обучение", 
                          callback_data='training_details_basic_program')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_basic_program')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

mobile_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Mobile - разработчик", 
                          callback_data='about_direction_mobile')],
    [InlineKeyboardButton(text="Подробность про обучение", 
                          callback_data='training_details_mobile')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_mobile')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

manager_project_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Менеджер Проектов", 
                          callback_data='about_direction_manager_project')],
    [InlineKeyboardButton(text="Подробность про обучение", 
                          callback_data='training_details_manager_project')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_manager_project')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

fullstack_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Fullstack - разработчик", 
                          callback_data='about_direction_fullstack')],
    [InlineKeyboardButton(text="Подробность про обучение", 
                          callback_data='training_details_fullstack')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_fullstack')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])

program_child_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="О направлении Программирование для детей", 
                          callback_data='about_direction_program_child')],
    [InlineKeyboardButton(text="Подробность про обучение", 
                          callback_data='training_details_program_child')],
    [InlineKeyboardButton(text="Стоимость обучение", callback_data='course_cost_program_child')],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_direction')]])