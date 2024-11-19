from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    
about_us_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="О Geeks:", callback_data='about_geeks')],
        [InlineKeyboardButton(text='Преимущества', callback_data='advantages')],
        [InlineKeyboardButton(text="После окончание курсов", 
        callback_data='after_graduation_course')]])


contact_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Бишкек', callback_data='bishkek'),
    InlineKeyboardButton(text='Ош', callback_data='osh')],
    [InlineKeyboardButton(text='Кара-балта', callback_data='kara-balta'),
    InlineKeyboardButton(text='Ташкент', callback_data='tashkent')],])

send_bishkek_local_and_contact_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Получить контакт", callback_data='send_contact_bishkek')],
    [InlineKeyboardButton(text="Получить локацию",
    url="https://www.google.com/maps?q=42.879149867099095,74.6184294271517")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_contact')]])

send_osh_local_and_contact_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Получить контакт", callback_data='send_contact_osh')],
    [InlineKeyboardButton(text="Получить локацию", 
    url="https://www.google.com/maps?q=40.51933469510711,72.80300035401469")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_contact')]])


send_kara_balta_local_and_contact_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Получить контакт", callback_data='send_contact_kara-balta')],
    [InlineKeyboardButton(text="Получить локацию",
    url="https://www.google.com/maps?q=42.80362749335512,73.85084189284159")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_contact')]])

send_tashkent_local_and_contact_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Получить контакт", callback_data='send_contact_tashkent')],
    [InlineKeyboardButton(text="Получить локацию", 
    url="https://www.google.com/maps?q=41.29536247898833,69.22550631172587")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data='back_contact')]])

