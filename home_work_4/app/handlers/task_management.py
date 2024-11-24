from aiogram import Router, F
from aiogram.filters import  Command, or_f, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums import ParseMode

from sqlalchemy.ext.asyncio import AsyncSession


from app.database.query_db import get_text_db, task_add, clear_task, get_desc_for_name
from app.keyboards.inline import show_tasks
from app.keyboards.reply import del_reply_kb, reply_kb
from app.middlewares.check_user_register import CheckRegister

router_1 = Router()
router_1.message.middleware(CheckRegister())

class StateTask(StatesGroup):
    name_task = State()
    description_task = State()


@router_1.message(StateFilter(None), or_f(Command('add_task'),(F.text.lower() == 'добавить задачу')))
async def add_tasks(message: Message, state: FSMContext, session):
    text = await get_text_db(session, id=8)
    await message.answer(text,parse_mode=ParseMode.HTML, reply_markup= del_reply_kb)
    await state.set_state(StateTask.name_task)


@router_1.message(StateTask.name_task, F.text)
async def task_name(message: Message, state: FSMContext, session):
    await state.update_data(name_task=message.text)
    text = await get_text_db(session, id=9)
    await message.answer(text, parse_mode=ParseMode.HTML)
    await state.set_state(StateTask.description_task)

@router_1.message(StateTask.name_task)
async def task_not_text(message: Message):
    await message.answer("<b>⚠️ Ошибка!</b> Введите <i>название задачи</i>.",
                         parse_mode=ParseMode.HTML)
    
    
@router_1.message(StateTask.description_task, F.text)
async def description_task(message: Message, state: FSMContext, session: AsyncSession):
    await state.update_data(description_task=message.text)
    await message.answer("Вы успешно создали задачу", reply_markup=await reply_kb())
    data = await state.get_data()
    await task_add(session, message, data)
    await state.clear()

    
@router_1.message(StateTask.description_task)
async def task_not_txt(message: Message):
    await message.answer("<b>⚠️ Ошибка!</b> Введите <i>текстовое описание</i> задачи.",
                         parse_mode=ParseMode.HTML)
    
    
@router_1.message(or_f(Command('show_tasks'), (F.text.lower() == 'показать задачи')))
async def task_show(message: Message, session):
    tasks = await show_tasks(session)
    if tasks:
        await message.answer(
        "<b>✨ Ваши задачи:</b> <i>Вот список всех текущих задач, которые вы добавили!</i>",
        reply_markup=tasks, parse_mode=ParseMode.HTML)

    else:
        await message.answer("У вас нет задач")
    
    

@router_1.message(or_f(Command('clear_task'), (F.text.lower() == "очистить список задач")))
async def add_task(message: Message, session):
    await clear_task(session, message.from_user.id)
    await message.answer("<b>✅ Успешно удалено!</b> <i>Задача была удалена из списка.</i>",
                        parse_mode=ParseMode.HTML)
    
    
@router_1.callback_query(F.data.startswith("task_"))
async def show_task_description(callback: CallbackQuery, session):
    await callback.answer("Описание задачи")
    task_id = int(callback.data.split("_")[1]) 
    desc_task = await get_desc_for_name(session, task_id)
    
    if desc_task:
        await callback.message.edit_text(
        f"<b>📝 Описание задачи:</b>:\n{desc_task.description}\n\n<b>📝 Имя задачи:</b>: {desc_task.name_task}",
        parse_mode=ParseMode.HTML)
    else:
        await callback.message.answer(
    "<b>❌ Задача не найдена!", parse_mode=ParseMode.HTML)
        
    
