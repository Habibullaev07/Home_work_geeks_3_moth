import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from app.handlers.handlers_for_send_email import router

load_dotenv(find_dotenv())

async def main():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
