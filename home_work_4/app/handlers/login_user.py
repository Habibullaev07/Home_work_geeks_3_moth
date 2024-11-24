import re
import asyncio

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.enums import ParseMode


from app.keyboards.inline import login_kb
from app.keyboards.reply import reply_kb
from app.database.query_db import orm_register, check_user_login, check_name, get_text_db

router_2 = Router()

class Registration(StatesGroup):
    username = State()
    password = State()
    
    
class Login(StatesGroup):
    get_username = State()
    get_password = State()
    
    
@router_2.message(CommandStart())
async def start_cmd(message: Message, session):
    text = await get_text_db(session, id=1)
    await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=await login_kb())


@router_2.callback_query(StateFilter(None), F.data == 'register')
async def register(callback: CallbackQuery, state: FSMContext, session):
    await callback.answer("Регистрация")
    text = await get_text_db(session, id=2)
    await callback.message.edit_text(text,
    parse_mode=ParseMode.HTML)
    await state.set_state(Registration.username)
    

@router_2.message(Registration.username, F.text)
async def reg_username(message: Message, state: FSMContext, session: AsyncSession):
    if re.match("^[A-Za-z0-9]{6,}+$", message.text):
        username = await check_name(session, message)
        text = await get_text_db(session, id=4)
        if username:
            await message.answer(text, parse_mode=ParseMode.HTML)
            return
        await state.update_data(username=message.text)
        text = await get_text_db(session, id=3)
        await message.answer(text, parse_mode=ParseMode.HTML)
        await state.set_state(Registration.password)        
    else:
        await message.answer("<b>Пожалуйста, введите корректные данные:</b>", 
                             parse_mode=ParseMode.HTML)
        
        
@router_2.message(Registration.username)
async def not_valid_username(message: Message):
    await message.answer("<b>❌ Ошибка!</b> <i>Введите корректные данные.</i>",
                         parse_mode=ParseMode.HTML)


@router_2.message(Registration.password, F.text)
async def reg_password(message: Message, state: FSMContext, session: AsyncSession):
    
    if re.match("^[A-Za-z0-9]{8,}+$", message.text):
        await state.update_data(password=message.text)
        text_1 = await get_text_db(session, id=5)
        await message.answer(text_1, parse_mode=ParseMode.HTML)
        await asyncio.sleep(3)
        text_2 = await get_text_db(session, id=6)
        await message.answer(text_2, parse_mode=ParseMode.HTML, reply_markup=await login_kb())
        data = await state.get_data()
        await orm_register(session, message, data)
        await state.clear()
    else:
        await message.answer("<b>Пожалуйста, введите корректные данные:</b>", 
                            parse_mode=ParseMode.HTML)
        
        
@router_2.message(Registration.password)
async def not_valid_password(message: Message):
    await message.answer("<b>❌ Ошибка!</b> <i>Введите корректные данные.</i>",
                         parse_mode=ParseMode.HTML)
    
    
@router_2.callback_query(StateFilter(None), F.data == 'login')
async def login(callback: CallbackQuery, state: FSMContext, session):
    await callback.answer("Пожалуйста, авторизуйтесь, чтобы продолжить.")
    text = await get_text_db(session, id=7)
    await callback.message.edit_text(text, parse_mode=ParseMode.HTML)
    await state.set_state(Login.get_username)
    
    
@router_2.message(Login.get_username)
async def get_username(message: Message, state:FSMContext):
    await state.update_data(get_username=message.text)
    await message.answer("<b>🔑 Пожалуйста, введите ваш <i>пароль</i> для продолжения:</b>",
                         parse_mode=ParseMode.HTML)
    await state.set_state(Login.get_password)


@router_2.message(Login.get_password, F.text)
async def get_password(message: Message, state: FSMContext, session: AsyncSession):
    data = await state.get_data()
    username = data.get("get_username")  
    password = message.text      
    check_users =  await check_user_login(session, username, password)  

    if check_users:
        await message.answer("<b>🎉 Поздравляем!</b> <i>Вы успешно вошли в систему!</i> 🎊", 
        parse_mode=ParseMode.HTML, reply_markup=await reply_kb())
        await state.clear() 
    else:
        await state.clear()
        await asyncio.sleep(1)
        await message.answer(
        "<b>⚠️ Упс!</b> <i>Неверное имя пользователя или пароль. Попробуйте снова.</i> 🔄", 
        parse_mode=ParseMode.HTML, reply_markup=await login_kb())


