import os
import asyncio

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from app.keyboards.reply import reply_menu_kb
from app.keyboards.inline import menu_inline_kb
from app.send_email import send_email
from app.html import html_for_message, html_for_audio, html_for_video, html_for_photo

router = Router()

class SendText(StatesGroup):
    gmail = State()
    text = State()
    
class SendPhoto(StatesGroup):
    gmail = State()
    photo = State()
    
class SendVideo(StatesGroup):
    gmail = State()
    video = State()
    
class SendAudio(StatesGroup):
    gmail = State()
    audio = State()
    
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
    "<b>🚀 Здравствуйте, вы находитесь на боте для отправки файлов и сообщений! 🚀</b>\n"
    "<i>📂 Отправка файлов и 📩 отправка сообщений — это просто и удобно!</i>",
    parse_mode=ParseMode.HTML, reply_markup=await reply_menu_kb())


@router.message(StateFilter(None), F.text.lower() == "отправка сообщение")
async def send_text(message: Message, state: FSMContext):
    await message.answer("<b>📧 Пожалуйста, отправьте ваш Gmail адрес:</b>",
    parse_mode=ParseMode.HTML)
    await state.set_state(SendText.gmail)
    
    
@router.message(SendText.gmail, F.text.contains("@gmail.com"))
async def state_send_text_1(message: Message, state: FSMContext):
    await state.update_data(gmail=message.text)
    await message.answer("<b>💬 Напишите свой текст для отправки👇</b>", parse_mode=ParseMode.HTML)
    await state.set_state(SendText.text)

@router.message(SendText.gmail)
async def check_text_1(message: Message):
    await message.answer("<b>⚠️ Пожалуйста, введите корректные данные:</b>", 
    parse_mode=ParseMode.HTML)


@router.message(SendText.text, F.text)
async def state_send_text_2(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await asyncio.sleep(0.5)
    await message.answer(
    "<b>✅ Ваш запрос успешно отправлен!</b>\n"
    "Пожалуйста, ожидайте 1-2 минуты. Мы обязательно обработаем ваш запрос в ближайшее время.", 
    parse_mode=ParseMode.HTML)
    html_content = html_for_message.format(message_text=data['text'])
    await send_email(
    recipient=data["gmail"],
    subject="🌟 Новое сообщение от бота 📩",
    message_body=html_content)
    await state.clear()


@router.message(SendText.text)
async def check_text_2(message: Message):
    await message.answer("<b>⚠️ Пожалуйста, введите корректные данные:</b>",
    parse_mode=ParseMode.HTML)
    
    
@router.message(F.text.lower() == "отправка различных файлов")
async def send_various_files(message: Message):
    await message.answer("<b>📤 Выберите тип отправки:</b>", 
    parse_mode=ParseMode.HTML, reply_markup=await menu_inline_kb())

    
@router.callback_query(F.data == "sending_photo")
async def sending_photo(callback: CallbackQuery, state: FSMContext):
    await callback.answer("получение Gmail")
    await callback.message.edit_text("<b>📧 Введите вашу электронную почту:</b>",
    parse_mode=ParseMode.HTML)
    await state.set_state(SendPhoto.gmail)


@router.message(SendPhoto.gmail, F.text.contains("@gmail.com"))
async def state_send_photo_1(message: Message, state: FSMContext):
    await state.update_data(gmail=message.text)
    await message.answer("<b>🖼️ Отправьте фото, которое хотите передать:</b>",
    parse_mode=ParseMode.HTML)
    await state.set_state(SendPhoto.photo)
    
    
@router.message(SendPhoto.gmail)
async def check_photo_1(message: Message):
    await message.answer("<b>⚠️ Пожалуйста, введите корректные данные:</b>",
    parse_mode=ParseMode.HTML)
    
    
@router.message(SendPhoto.photo, F.photo)
async def state_send_photo_2(message: Message, state: FSMContext, bot: Bot):
    await asyncio.sleep(0.5)
    await message.answer(
    "<b>✅ Ваш запрос успешно отправлен!</b>\n"
    "Пожалуйста, ожидайте 1-2 минуты. Мы обязательно обработаем ваш запрос в ближайшее время.", 
    parse_mode=ParseMode.HTML)
    
    data = await state.get_data()
    gmail = data["gmail"]
    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = f"./{photo.file_id}.jpg"
    await bot.download_file(file.file_path, file_path)
    await send_email(
        recipient=gmail,
        subject='📸 Новое фото',
        message_body=html_for_photo,
        send_file=file_path)
    
    if os.path.exists(file_path):
        os.remove(file_path)
    await state.clear()

@router.message(SendPhoto.photo)
async def check_photo_2(message: Message):
    await message.answer("<b>⚠️ Пожалуйста, введите корректные данные:</b>",
    parse_mode=ParseMode.HTML)


@router.callback_query(F.data == "sending_video")
async def sending_video(callback: CallbackQuery, state: FSMContext):
    await callback.answer("получение Gmail")
    await callback.message.edit_text("<b>📧 Введите вашу электронную почту:</b>",
    parse_mode=ParseMode.HTML)
    await state.set_state(SendVideo.gmail)


@router.message(SendVideo.gmail, F.text.contains("@gmail.com"))
async def state_send_video_1(message: Message, state: FSMContext):
    await state.update_data(gmail=message.text)
    await message.answer("<b>🎥 Отправьте видео, которое вы хотите передать:</b>",
    parse_mode=ParseMode.HTML)
    await state.set_state(SendVideo.video)
    
    
@router.message(SendVideo.gmail)
async def check_video_1(message: Message):
    await message.answer("<b>⚠️ Пожалуйста, введите корректные данные:</b>",
    parse_mode=ParseMode.HTML)
    
    
@router.message(SendVideo.video, F.video)
async def state_send_video_2(message: Message, state: FSMContext, bot: Bot):
    await asyncio.sleep(0.5)
    await message.answer(
    "<b>✅ Ваш запрос успешно отправлен!</b>\n"
    "Пожалуйста, ожидайте 1-2 минуты. Мы обязательно обработаем ваш запрос в ближайшее время.", 
    parse_mode=ParseMode.HTML)
    
    data = await state.get_data()
    gmail = data["gmail"]
    video = message.video
    video_id = video.file_id
    file = await bot.get_file(video_id)

    video_path = f"./{video_id}.mp4"
    await bot.download_file(file.file_path, video_path)
    await send_email(
        recipient=gmail,
        subject="🎥 Новое видео успешно отправлено",
        message_body=html_for_video,
        send_file=video_path)
    
    if os.path.exists(video_path):
        os.remove(video_path)
    await state.clear()

@router.message(SendVideo.video)
async def check_video_2(message: Message):
    await message.answer("<b>⚠️ Пожалуйста, введите корректные данные:</b>",
    parse_mode=ParseMode.HTML)
    
    
@router.callback_query(F.data == "sending_audio")
async def sending_audio(callback: CallbackQuery, state: FSMContext):
    await callback.answer("получение gmail")
    await callback.message.edit_text("<b>📧 Введите вашу электронную почту:</b>",
    parse_mode=ParseMode.HTML)
    await state.set_state(SendAudio.gmail)


@router.message(SendAudio.gmail, F.text.contains("@gmail.com"))
async def state_send_audio_1(message: Message, state: FSMContext):
    await state.update_data(gmail=message.text)
    await message.answer("<b>🎵 Отправьте аудио, которое хотите передать:</b>",
    parse_mode=ParseMode.HTML, reply_markup=await reply_menu_kb())
    await state.set_state(SendAudio.audio) 
    
@router.message(SendAudio.gmail)
async def check_audio_1(message: Message):
    await message.answer("<b>⚠️ Пожалуйста, введите корректные данные:</b>",
    parse_mode=ParseMode.HTML)
    

@router.message(SendAudio.audio, F.audio)
async def state_send_audio_2(message: Message, state: FSMContext, bot: Bot):
    await asyncio.sleep(0.5)
    await message.answer(
    "<b>✅ Ваш запрос успешно отправлен!</b>\n"
    "Пожалуйста, ожидайте 1-2 минуты. Мы обязательно обработаем ваш запрос в ближайшее время.", 
    parse_mode=ParseMode.HTML)
    
    data = await state.get_data()
    gmail = data["gmail"]
    audio = message.audio
    audio_id = audio.file_id
    file = await bot.get_file(audio_id)
    audio_path = f"./{audio_id}.mp3"
    await bot.download_file(file.file_path, audio_path)
    
    await send_email(
        recipient=gmail,
        subject="🎶 Новое аудио успешно отправлено",
        message_body=html_for_audio,
        send_file=audio_path)
    
    if os.path.exists(audio_path):
        os.remove(audio_path)
        
    await state.clear()

@router.message(SendAudio.audio)
async def check_audio_2(message: Message):
    await message.answer("<b>⚠️ Пожалуйста, введите корректные данные:</b>",
    parse_mode=ParseMode.HTML)