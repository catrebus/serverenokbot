import asyncio

from aiogram import Bot, Dispatcher

from config import Config
from handlers import bot_router

bot = Bot(Config.BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(bot_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass