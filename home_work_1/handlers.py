import time
import random

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup 


router = Router()

photo_win = "https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg"

numbers = random.randint(1, 100)
attempts = 5

class GameGuessNumber(StatesGroup):
    lets_start_game = State()
    first_handler = State()
    two_handler = State()
    three_handler = State()
    four_handler = State()

async def more_or_less_hint(message: types.Message, message_text):
    if message_text > numbers:
        await message.answer(f"Данное число 👉 {message_text} - больше🔹\nВедите наименьшее число")
    else:
        await message.answer(f"Данное число 👉 {message_text} - меньше🔸\nВедите наибольшее число")
    time.sleep(0.5)
    
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(text=f"Привет - {message.from_user.first_name}")
    await message.answer(text="Вы готовы играть угадай число от 1 до 100?")
    await message.answer(text="просто ведите 'да' или нажмите на команду /start_game ")

@router.message(or_f(Command('start_game'), F.text.lower().contains('да')))
async def game_started(message: types.Message, state: FSMContext):
    global attempts, numbers
    numbers = random.randint(1, 100)
    attempts = 5
    await message.answer(text="Я загадал число от 1 до 100 угадайте! \nу вас есть 5 попыток")
    await state.set_state(GameGuessNumber.lets_start_game)

@router.message(GameGuessNumber.lets_start_game)
async def attempt_1(message: types.Message, state: FSMContext):
    global attempts
    try:
        massage_text = int(message.text)
    except ValueError:
        await message.answer(f"Ведите только числа \n{message.from_user.first_name}. ") 
        return
    if massage_text != numbers:
        attempts -= 1 
        await more_or_less_hint(message, massage_text)
        await message.answer(f"Осталось попытки - {attempts}")
        await state.set_state(GameGuessNumber.first_handler)
    else:
        await message.answer("Вы угадали число")
        time.sleep(1)
        await message.answer_photo(photo_win)
        await message.answer('Поздравляю')
        await state.clear()


@router.message(GameGuessNumber.first_handler)
async def attempt_2(message: types.Message, state: FSMContext):
    global attempts
    try:
        massage_text = int(message.text)
    except ValueError:
        await message.answer(f"Ведите только числа \n{message.from_user.first_name}. ") 
        return 
    if massage_text != numbers:
        attempts -= 1 
        await more_or_less_hint(message, massage_text)
        await message.answer(f"Осталось попытки - {attempts}")
        await state.set_state(GameGuessNumber.two_handler)    
    else:
        await message.answer("Вы угадали число")
        time.sleep(1)
        await message.answer_photo(photo_win)
        await message.answer('Поздравляю')
        await state.clear()
    
@router.message(GameGuessNumber.two_handler)
async def attempt_3(message: types.Message, state: FSMContext):
    global attempts
    try:
        massage_text = int(message.text)
    except ValueError:
        await message.answer(f"Ведите только числа \n{message.from_user.first_name}. ") 
        return
    if massage_text != numbers:
        attempts -= 1 
        await more_or_less_hint(message, massage_text)
        await message.answer(f"Осталось попытки - {attempts}")
        await state.set_state(GameGuessNumber.three_handler)
    else:
        await message.answer("Вы угадали число")
        time.sleep(1)
        await message.answer_photo(photo_win)
        await message.answer('Поздравляю')
        await state.clear()

@router.message(GameGuessNumber.three_handler)
async def attempt_4(message: types.Message, state: FSMContext):
    global attempts
    try:
        massage_text = int(message.text)
    except ValueError:
        await message.answer(f"Ведите только числа \n{message.from_user.first_name}. ") 
        return
    if massage_text != numbers:
        attempts -= 1 
        await more_or_less_hint(message, massage_text)
        await message.answer(f"Осталось попытки - {attempts}")
        await state.set_state(GameGuessNumber.four_handler)
    else:
        await message.answer("Вы угадали число")
        time.sleep(1)
        await message.answer_photo(photo_win)
        await message.answer('Поздравляю')
        await state.clear()
        
@router.message(GameGuessNumber.four_handler)
async def attempt_5(message: types.Message, state: FSMContext):
    global attempts
    try:
        massage_text = int(message.text)
    except ValueError:
        await message.answer(f"Ведите только числа \n{message.from_user.first_name}. ") 
        return
    if massage_text != numbers: 
        await message.answer("Вы не угадали число 😌\nу вас не осталось попыток игра закончено!")
        time.sleep(1)
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")
        time.sleep(1)
        await message.answer(f"Кстати число было {numbers}😁")
        await message.answer("Нажмите команду 👉/start_game что бы заново начать")
        await state.clear()
    else:
        await message.answer("Вы угадали число")
        time.sleep(1)
        await message.answer_photo(photo_win)
        await message.answer('Поздравляю')
        await state.clear()
