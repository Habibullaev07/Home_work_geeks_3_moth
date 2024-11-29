import re
import asyncio

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import CommandStart, StateFilter

from app.database.quary_db import register_user_db, get_username, get_text_from_db
from app.keyboards.inline import auth_keyboard
from app.keyboards.reply import menu_kb

router_1 = Router()

temp_storage = {}

class Register(StatesGroup):
    name = State()
    username = State()
    password = State()
    
class Login(StatesGroup):
    check_username = State()
    check_password = State()
    
@router_1.message(CommandStart())
async def cmd_start(message: Message, session):
    text = await get_text_from_db(session, 1)
    await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=await auth_keyboard())


@router_1.callback_query(StateFilter(None), F.data == 'register')
async def register(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Регистрация")
    await callback.message.answer(
    "<b>👋 Привет! Как тебя зовут? Напиши ниже, чтобы мы могли продолжить 🚀</b>",
    parse_mode=ParseMode.HTML)
    await state.set_state(Register.name)


@router_1.message(Register.name, F.text)
async def state_reg_1(message: Message, state: FSMContext):
    if re.match("^[A-Za-zА-Яа-яЁё]+$", message.text):
        await state.update_data(name=message.text)
        await message.answer("<b>🔑 Введите свой username, чтобы продолжить!</b>",
        parse_mode=ParseMode.HTML)
        await state.set_state(Register.username)
    else:
        await message.answer("<b>❌ Недопустимые символы. Введите только буквы.</b>",
        parse_mode=ParseMode.HTML)
    
@router_1.message(Register.name)
async def check_state_reg_step_1(message: Message):
    await message.answer("<b>❌ Введены некорректные данные. Пожалуйста, попробуйте снова.</b>",
    parse_mode=ParseMode.HTML)


@router_1.message(Register.username, F.text)
async def state_reg_2(message: Message, state: FSMContext, session):
    username = await get_username(session, message.text)
    if not username:
        if re.match("^[A-Za-z0-9_]{6,}+$", message.text):
            await state.update_data(username=message.text)
            await message.answer("<b>🔒 Введите новый пароль для вашего аккаунта.</b>",
            parse_mode=ParseMode.HTML)
            await state.set_state(Register.password)
        else:
            await message.answer(
            "<b>❌ Используйте только буквы, цифры и подчеркивания. Минимум 6 символов.</b>",
            parse_mode=ParseMode.HTML)
            return
    else:
        await message.answer(
        "<b>❌ Это имя пользователя уже занято. Пожалуйста, выберите другое.</b>",
        parse_mode=ParseMode.HTML)

@router_1.message(Register.username)
async def check_state_reg_step_2(message: Message):
    await message.answer("<b>❌ Введены некорректные данные. Пожалуйста, попробуйте снова.</b>",
    parse_mode=ParseMode.HTML)
    

@router_1.message(Register.password, F.text)
async def state_reg_3(message: Message, state: FSMContext, session):
    if re.match("^[A-Za-z0-9]{8,}+$", message.text):
        await state.update_data(password=message.text)
        await message.answer("<b>🎉 Поздравляем, вы успешно зарегистрированы! 🚀</b>",
        parse_mode=ParseMode.HTML)
        await asyncio.sleep(2)
        await message.answer(
        "<i>Теперь войдите в свой аккаунт, чтобы начать пользоваться всеми функциями.</i>",
        parse_mode=ParseMode.HTML, reply_markup=await auth_keyboard())
        data = await state.get_data()
        await register_user_db(session, message, data)
        await state.clear()
    else:
        await message.answer(
        "❌ Некорректные данные. Используйте только буквы и цифры (не менее 8 символов).",
        parse_mode=ParseMode.HTML)

@router_1.message(Register.password)
async def check_state_reg_step_3(message: Message):
    await message.answer("<b>❌ Введены некорректные данные. Пожалуйста, попробуйте снова.</b>",
    parse_mode=ParseMode.HTML)


@router_1.callback_query(StateFilter(None), F.data == 'login')
async def login(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Авторизация")
    await callback.message.answer(
    "<b>🔑 Введите ваш username для авторизации.</b>", parse_mode=ParseMode.HTML)
    await state.set_state(Login.check_username)


@router_1.message(Login.check_username, F.text)
async def state_login_1(message: Message, state: FSMContext):
    await state.update_data(check_username=message.text)
    await message.answer("<b>🔒 Введите свой пароль для входа.</b>", parse_mode=ParseMode.HTML)
    await state.set_state(Login.check_password)
    
@router_1.message(Login.check_username)
async def check_login_step_1(message: Message):
    await message.answer("<b>❌ Введены некорректные данные. Пожалуйста, попробуйте снова.</b>",
    parse_mode=ParseMode.HTML)
    

@router_1.message(Login.check_password, F.text)
async def state_login_2(message: Message, state: FSMContext, session):
    check_password = message.text
    data = await state.get_data()
    data_username = data.get('check_username')
    get_info_user = await get_username(session, data_username)   
    if get_info_user is not None and get_info_user.password == check_password:
        temp_storage['username'] = data_username
        await state.update_data(check_password=message.text)
        await message.answer(f'''<b>🏦 Добро пожаловать в AurumVault!</b>, {data_username}!
<b>💰 Ваш текущий баланс: {get_info_user.balance:,.0f} сомов.</b>'''.replace(',', '.'), parse_mode=ParseMode.HTML,
        reply_markup=await menu_kb())
        await state.clear()
    else:
        await message.answer(
        "<b>❌ Введены неверные имя пользователя или пароль. Пожалуйста, повторите попытку.</b>",
        parse_mode=ParseMode.HTML, reply_markup=await auth_keyboard())
        await state.clear()

@router_1.message(Login.check_password)
async def check_login_step_2(message: Message):
   await message.answer("<b>❌ Введены некорректные данные. Пожалуйста, попробуйте снова.</b>",
    parse_mode=ParseMode.HTML)
