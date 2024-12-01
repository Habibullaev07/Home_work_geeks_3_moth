import os
import asyncio
import logging

from aiogram import Bot, Dispatcher 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from app.database.engine import create_db, clear_db, async_session
from app.middleware.database import DataBaseSession
from app.handlers.admin_private import admin_private_router
from app.handlers.user_group import user_group_router
from app.handlers.user_private import user_private_router
from app.command.commands import command

async def on_startup(bot):
     
    run_param = False
    if run_param:
        await clear_db()
    await create_db()
    
async def on_shutdown(bot):
    print("Бот завершил работу")
    
async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    bot.my_admins_list = []
    dp = Dispatcher()
    
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=async_session))
    dp.include_routers(admin_private_router, user_group_router, user_private_router)
    logging.basicConfig(level=logging.INFO)
    await bot.set_my_commands(commands=command)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
