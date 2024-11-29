import re
import asyncio

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup

from app.database.quary_db import  get_username,  update_password, get_text_from_db
from app.keyboards.inline import top_up_request_kb
from app.middleware.check_user import Check_user
from app.handlers.auth_users import temp_storage
from app.keyboards.reply import del_reply_kb, menu_kb


router_2 = Router()
router_2.message.middleware(Check_user())
   
class Change_Password(StatesGroup):
    old_password = State()
    new_password = State()

class Transfer_money(StatesGroup):
    username_for_transfer = State()
    transfer_amount = State()
    
class Replenishment_Money(StatesGroup):
    replenishment_amount = State()
    
def get_temp_storage():
    return temp_storage.get('username')


@router_2.message(F.text.lower() == "просмотр баланса")
async def view_balance(message: Message, session):
    username = get_temp_storage()
    balance = await get_username(session, username)
    # balance = round(get_balance.balance, 2)
    await message.answer(f"💰 <b>Ваш баланс: {balance.balance:,.0f} сомов</b>".replace(',', '.'),
    parse_mode=ParseMode.HTML)
    

@router_2.message(StateFilter(None), F.text.lower() == "пополнение счета")
async def replenishment_of_balance(message: Message, state: FSMContext, session):
    username = get_temp_storage()
    data_user = await get_username(session, username)
    if data_user.deposit_balance != 0:
        await message.answer(
    f"💸 <b>Доступные средства для пополнения:</b> {data_user.deposit_balance:,.0f}".replace(',', '.'),
        parse_mode=ParseMode.HTML)
        await asyncio.sleep(1)
        await message.answer("<b>💰 Введите сумму для пополнения счета:</b>", parse_mode=ParseMode.HTML,
        reply_markup=del_reply_kb)
        await state.set_state(Replenishment_Money.replenishment_amount)
    else:
        await message.answer(
    f"<b>💰 На вашем балансе</b> <i>{data_user.deposit_balance:,.0f}</i> <b>сомов.</b><br>".replace(',', '.'),
        parse_mode=ParseMode.HTML)
        await asyncio.sleep(1.5)
        await message.answer("<i>🚫 Вы исчерпали все средства для пополнения.</i>",
        parse_mode=ParseMode.HTML)  
    
    
@router_2.message(Replenishment_Money.replenishment_amount, F.text)
async def state_replenishment_balance(message: Message, state: FSMContext, session: AsyncSession):
    username = get_temp_storage()
    data_user = await get_username(session, username)
    deposit_balance = round(data_user.deposit_balance, 2)
    if message.text.isdigit():
        replenishment_amount = int(message.text)
        if deposit_balance >= replenishment_amount:
            data_user.deposit_balance -= replenishment_amount
            data_user.balance += replenishment_amount
            await state.update_data(replenishment_balance=replenishment_amount)
            await message.answer(
            f"🎉 <b>Успех!</b> Ваш баланс пополнен на <b>{replenishment_amount}</b> сомов! 💰",
            parse_mode=ParseMode.HTML, reply_markup=await menu_kb())
            await session.commit()
            await state.clear()
        else:
            await message.answer(
    f"❌ Недостаточно средств для пополнения на <b>{replenishment_amount}</b>. Попробуйте другую сумму.",
            parse_mode=ParseMode.HTML)
    else:
        await message.answer("⚠️ Пожалуйста, введите <b>только числа</b>. 🔢",
        parse_mode=ParseMode.HTML)
    
    
@router_2.message(StateFilter(None),F.text.lower() == 'перевод средств')
async def transfer_of_funds(message: Message, state: FSMContext):
    await message.answer("💸 Кому хотите перевести деньги? Напишите <b>username</b> пользователя.",
    reply_markup=del_reply_kb, parse_mode=ParseMode.HTML)
    await state.set_state(Transfer_money.username_for_transfer)

@router_2.message(Transfer_money.username_for_transfer, F.text)
async def state_transfer_step_1(message: Message, state: FSMContext, session):
    user_text = message.text
    username = await get_username(session, user_text)
    if  username:
        await state.update_data(recipient_username=user_text)
        await message.answer(f"💰 Сколько хотите перевести <b>{user_text}</b> пользователю?",
        parse_mode=ParseMode.HTML)
        await state.set_state(Transfer_money.transfer_amount)
    else:
        await message.answer("<b>⚠️ Внимание:</b> Пожалуйста, введите корректное имя пользователя!",
        parse_mode=ParseMode.HTML)
        return

@router_2.message(Transfer_money.transfer_amount)
async def state_transfer_step_2(message: Message, state: FSMContext, session):
    username = get_temp_storage()
    balance = await get_username(session, username)
    balance = round(balance.balance, 2)
    if balance >= 10:
        await state.update_data(transfer_amount=message.text)
        data = await state.get_data()
        await message.answer(
        "<b>⚠ Подтверждение требуется:</b> Пожалуйста, подтвердите, что хотите продолжить.",
        parse_mode=ParseMode.HTML)
        await asyncio.sleep(1.5)
        await message.answer(
        f"<b>💸 Вы отправляете этому пользователю:</b> {data['recipient_username']}",
        parse_mode=ParseMode.HTML)
        await asyncio.sleep(1)
        await message.answer(
        f"<b>💸 Сумма перевода:</b> {data['transfer_amount']} сомов",
        parse_mode=ParseMode.HTML, reply_markup=await top_up_request_kb())

    else:
        await message.answer(
        f"<b>❌ Недостаточно средств:</b> У вас на балансе всего {balance} сомов.")
        await asyncio.sleep(1)
        await message.answer(
        "<b>❗ Минимальная сумма:</b> Сумма перевода должна быть не менее 10 сомов.",
        parse_mode=ParseMode.HTML)


@router_2.callback_query(StateFilter('*'), F.data == 'cancellation')
async def cancel_state(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Отмена")
    await callback.message.answer("<b>✅ Вы успешно отменили операцию.</b>",
    parse_mode=ParseMode.HTML)
    await state.clear()

@router_2.callback_query(StateFilter('*'), F.data == 'yes_top_up')
async def confirmation(callback: CallbackQuery, state: FSMContext, session: AsyncSession):
    await callback.answer("Отправляется деньги")
    data = await state.get_data()
    transfer_amount = int(data['transfer_amount'])
    recipient_username = data['recipient_username']
    
    username_sender = get_temp_storage()
    sender = await get_username(session, username_sender)
    recipient_username = await get_username(session, recipient_username)
    
    sender.balance -= transfer_amount
    recipient_username.balance += transfer_amount
    await session.commit()
    await callback.message.answer(
    "<b>✅ Успешно прошло!</b> Ваша транзакция завершена без ошибок. Спасибо, что выбрали нас!",
    parse_mode=ParseMode.HTML, reply_markup=await menu_kb())
    await state.clear()


@router_2.message(StateFilter(None), F.text.lower() == 'смена пароля')
async def change_password(message: Message, state: FSMContext):
    await message.answer("<b>🔐 Старый пароль:</b> Введите ваш текущий пароль для продолжения.",
    parse_mode=ParseMode.HTML, reply_markup=del_reply_kb)
    await state.set_state(Change_Password.old_password)
    

@router_2.message(Change_Password.old_password, F.text)
async def change_pass_step_1(message: Message, state: FSMContext, session):
    old_password = message.text
    data_username = temp_storage.get('username')
    get_old_pass_with_db = await get_username(session, data_username)
    if get_old_pass_with_db.password ==  old_password:
        await state.update_data(old_password=old_password)
        await message.answer("<b>🔑 Новый пароль:</b> Введите ваш новый пароль для продолжения.",
        parse_mode=ParseMode.HTML)
        await state.set_state(Change_Password.new_password)
    else:
        await message.answer("<b>❌ Неверно введен пароль!</b> Пожалуйста, попробуйте снова.",
        parse_mode=ParseMode.HTML)

@router_2.message(Change_Password.old_password)
async def check_state_change_step_1(message: Message):
    await message.answer(
    "<b>❗ Введены неправильные данные!</b> Пожалуйста, проверьте и введите правильную информацию.",
    parse_mode=ParseMode.HTML)
    
@router_2.message(Change_Password.new_password, F.text)
async def change_pass_step_2(message: Message, state: FSMContext, session):
    new_pass = message.text
    data_username = temp_storage.get('username')
    if re.match("^[A-Za-z0-9_]{8,}+$", new_pass):
        await state.update_data(new_password=new_pass)
        await message.answer("<b>✅ Пароль обновлен!</b>", parse_mode=ParseMode.HTML,
        reply_markup=await menu_kb())
        data = await state.get_data()
        get_data_new_pass = data.get('new_password')
        await update_password(session, data_username, get_data_new_pass)
        await state.clear()
    else:
        text = await get_text_from_db(session, 3)
        await message.answer(text, parse_mode=ParseMode.HTML)

@router_2.message(Change_Password.new_password)
async def check_state_change_step_2(message: Message):
    await message.answer(
    "<b>❗ Введены неправильные данные!</b> Пожалуйста, проверьте и введите правильную информацию.",
    parse_mode=ParseMode.HTML)
    
@router_2.message(F.text.lower() == "выход из аккаунта")
async def logout_from_acount(message: Message):
    temp_storage.pop('username', None)
    await message.answer("<b>🚪 Вы вышли из аккаунта</b> <i>До скорых встреч! 👋</i>",
    parse_mode=ParseMode.HTML, reply_markup=del_reply_kb)
    await asyncio.sleep(1)
    await message.answer(
    "<b>🔑 Если захотите вернуться, используйте /start</b> <i>Мы всегда рады помочь! 🚀</i>",
    parse_mode=ParseMode.HTML)
    
    
    
    
    

    

        