from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import load_config
from other.texts import admin_lexicon
from database.database import create_table

admin_router = Router()
config = load_config()


@admin_router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(text=admin_lexicon['admin_start'])


@admin_router.message(Command(commands='table'))
async def table(message: Message):
    create_table('textik', 228)
    await message.answer(text='Таблица создана')
