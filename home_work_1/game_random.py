''' ЭТОМУ ВСЕМУ Я НАУЧИЛСЯ В ЮТУБЕ КРОМЕ State, StatesGroup, FSMContext ЭТИХ КЛАССОВ ЭТИ КЛАССЫ СЕГОДНЯ ИЗУЧИЛ
ВСЕ ВНИЗУ ОБЪЯСНИЛ ГДЕ НАУЧИЛСЯ И У КОГО,

НА ДАННУЮ ДОМАШКУ У МЕНЯ УШЛО БОЛЬШЕ 5 ЧАСОВ ОЧЕНЬ ХОРОШО ПОПРАКТИКОВАЛСЯ
ВРЕМЯ ОЧЕНЬ БЫСТРО ПРОЛЕТЕЛО НОЧЬЮ ДЕЛАЛ

ПРОСТО НАПИСАЛ ДЛЯ ТОГО ЧТОБЫ ВЫ НЕ УДИВЛЯЛИСЬ, И ВСЕ ОСТАЛЬНОЕ ВНИЗУ 👇 ''' 

import asyncio
import os

from aiogram import Bot, Dispatcher 

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers import router

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
        
''' ЭТУ ЖЕ УСЛОВИЮ if __name__ == '__main__': Я САМ ДЕЛАЛ ЭТО В ПЕРВОМ УРОКЕ ИСЛАМ НАС УЧИЛ ЧТО __NAME__ АВТОМАТИЧЕСКИ СОЗДАЕТСЯ 
В КАЖДЫЙ МОДУЛЬ ТО ЕСТЬ ПРИ СОЗДАНИЕ ФАЙЛА А __MAIN__ ЭТО ЗАПУСК В ДАННОМ МОДУЛЕ ТО ЕСТЬ МЫ ГОВОРИМ
ЧТО ХОТИМ ЗАПУСТИТЬ КОД ТОЛЬКО В ДАННОМ МОДУЛЯ ЭТО НУЖНО КАК Я ПОНИМАЮ ЧТО ПРИ ИМПОРТИРОВАНИЕ МОДУЛЯ
НЕ ЗАПУСКАЛСЯ ДАННЫЙ КОД КОТОРЫЙ МЫ ВЫЗЫВАЕМ ПОСЛЕ УСЛОВИЕ ЧТО МОДУЛЬ HOME_WORK1.PY ЗАПУСКАЛСЯ ТОЛЬКО
В САМОМ МОДУЛЕ А НЕ В КАКОМ ТО ДРУГОМ ЭТО ПОЛЕЗНО КОГДА МЫ БУДЕМ СОЗДАВАТЬ МНОГО ПАПОК ФАЙЛОВ ЧТО БЫ
КОГДА МЫ ИМПОРТИРОВАЛИ НЕ БЫЛО ТАКОГО ЧТО БЫ ДАННЫЕ КОДЕ ЗАПУСКАЛИСЬ ВОТ И ВСЕ
И ЕЩЕ ЧТО Я ПИСАЛ В КОДЕ ВОТ ЭТИ КЛАССЫ State, StatesGroup, FSMContext ИЗУЧАЛ В ИНТЕРНЕТЕ ЧТО И КАК РАБОТАЕТ 
А ДРУГИЕ КЛАССЫ Я ЗНАЛ
ЧЕРЕЗ ЮТУБ ИЗУЧАЛ СМОТРЕЛ КУРСЫ ТАМ ТОЖЕ ОДИН ЮТУБЕР ЕСТЬ МАКСИМАЛЬНО ПОДРОБНО ОБЪЯСНЯЕТ КАК РАБОТАТЬ
 С ДОКУМЕНТАЦИЕЙ И В САМОМ КУРСЕ СОЗДАЕТ ПРИЛОЖЕНИЕ ДЛЯ ПРОДАЖИ ЕДЫ У НЕГО ТОЖЕ 8 УРОКОВ ЗА ВОСЕМЬ УРОКОВ
 ПОЛНОСТЬЮ СОЗДАСТ ПРИЛОЖЕНИЕ ДЛЯ ЕДЫ ПРОДАЖИ ЗАКАЗОВ ТАКОГО ТЕЛЕГРАМ БОТА НЕ ПРИЛОЖЕНИЕ А БОТА 
 ДОШЕЛ ДО 5 УРОКА  6 УРОК НЕ СМОТРЕЛ ПРОЙДУ ТО ЧТО ИЗУЧАЛ ЕЩЕ РАЗ ПЕРЕСМОТРЮ ТАМ РАБОТА С БАЗА ДАННЫЙ
 И ТД ПОСЛЕ 5 ТОГО УРОКА СЛОЖНО ВСЕ ЗАПОМИНАТЬ ПЕРЕСМОТРЮ
 И  ВСЕ БУДУ ПОВТОРЯТЬ  tate, StatesGroup, FSMContext ЭТИ КЛАССЫ И ПРАКТИКОВАТЬСЯ ЧТОБЫ ПОЛНОСТЬЮ ОСВОИТЬ
 И ЕЩЕ Я ОЧЕНЬ ЗАМОРОЧИЛСЯ С КОДОМ МОЖНО БЫЛО ОКАЗЫВАЕТСЯ СДЕЛАТЬ ЕЩЕ ПРОЩЕ НЕ ПИСАТЬ ОТДЕЛЬНО ОБРАБОТЧИКИ 
 Я ПОТОМ УЗНАЛ ЧТО МОЖНО СДЕЛАТЬ ПОПРОЩЕ И ВСЕ ЗАМОРОЧКА ДАЛО МНЕ БОЛЬШЕ ТЕОРИИ ЧЕМ ТО ЧТО ЕСЛИ Я БЫ ЗНАЛ 
 БЫ СДЕЛАТЬ ПОПРОЩЕ Я БЫ ТАК ПОНЯТНО НЕ ПОНЯЛ БЫ КАК ЩАС И ВСЕ. СПАСИБО ЗА УРОКИ И ВОТ САМ КАНАЛ ГДЕ Я УЧУСЬ
 ТАМ ТОЖЕ 8 УРОКОВ НА ГИТ ХАБ ТОЖЕ ЗАГРУЖЕНЫ У НЕГО  ВСЕ УРОКИ
 https://www.youtube.com/@PythonHubStudio ВОТ КАНАЛ
 https://github.com/PythonHubStudio/aiogram-3-course-telegram-bot.git ВОТ ЕГО ГИТ ХАБ 
 МНОГО ЧЕГО ИЗУЧИЛ ДЛЯ СЕБЯ В ДАННЫХ УРОКАХ
 
 ИЗУЧАЮ УЖЕ НЕДЕЛЮ МНОГО ЧЕГО ИЗУЧИЛ 
 НО НАДО ПОВТОРИТЬ ЧТО ИЗУЧАЛ Я МАЛО ПРАКТИКИ ДЕЛАЮ НАДО ПОБОЛЬШЕ ДЕЛАТЬ

 '''
# НА ДАННУЮ ДОМАШКУ У МЕНЯ УШЛО БОЛЬШЕ 5 ЧАСОВ НЕ ЗНАЮ КАК НО БЫСТРО ВРЕМЯ ПРОШЛО
  
  

