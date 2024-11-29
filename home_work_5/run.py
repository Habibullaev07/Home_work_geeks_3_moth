import os
import asyncio
import logging

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from app.database.engine import create_db, clear_db, async_session
from app.middleware.database import DataBaseSession
from app.handlers.auth_users import router_1
from app.handlers.menu import router_2
from app.command.command import command

async def on_startup(bot):
    
    run_param = False
    if run_param:
        await clear_db()
    await create_db()
    
    
    
async def on_shutdown(bot):
    print("Бот завершил работу")
    
async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=async_session))
    dp.include_routers(router_1, router_2)
    logging.basicConfig(level=logging.INFO)
    await bot.set_my_commands(commands=command)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
