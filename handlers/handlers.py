from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from utils import get_cpu_temp

bot_router = Router()

@bot_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Бот готов к работе")

@bot_router.message(Command('sensors'))
async def cmd_sensors(message: Message):
    await message.answer(f"{get_cpu_temp()}")