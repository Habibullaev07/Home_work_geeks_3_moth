import os, asyncio, logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.handlers.task_management import router_1
from app.handlers.login_user import router_2
from app.command.commands import command

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
  
from app.middlewares.database import DataBaseSession


from app.database.run_db import create_db, drop_db, session_maker

bot = Bot(token=os.getenv('TOKEN'))

async def start_bot(bot):
    
    clear_db = False
    if clear_db:
        await drop_db()
    await create_db()
    
    
async def shutdown_bot(bot):
    print("Выключен")
    
async def main():
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.startup.register(start_bot)
    dp.shutdown.register(shutdown_bot)
    dp.update.middleware(DataBaseSession(session=session_maker))
    dp.include_router(router_1)
    dp.include_router(router_2)
    logging.basicConfig(level=logging.INFO)
    await bot.set_my_commands(commands=command)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')