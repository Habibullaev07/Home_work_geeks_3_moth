from typing import Awaitable, Any, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from sqlalchemy.ext.asyncio import async_sessionmaker

class DataBaseSession(BaseMiddleware):
    def __init__(self, session: async_sessionmaker):
        self.session = session
    
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],    
    ) -> Any:
        async with self.session() as session:
            data['session'] = session
            return await handler(event, data)