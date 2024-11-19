import asyncio 
import os
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers.handlers import router1
from app.handlers.handlers_direction.first_3_directions import router2
from app.handlers.handlers_direction.second_3_directions import router3
from app.handlers.handlers_direction.third_3_directions import router4
from app.handlers.handlers_direction.last_4_directions import router5

from app.command import command


load_dotenv(os.path.join("..", "home_work_1", ".env"))

async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router1, router2, router3, router4, router5)
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(True)
    await bot.set_my_commands(commands=command)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')