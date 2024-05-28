from aiogram import Router, F, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.enums import ParseMode

from config import load_config
from other.texts import admin_lexicon
from database.database import create_table
from .kb import create_keyboard
from .filters.admin_check import AdminIdsFilter

admin_router = Router()
config = load_config()

admin_router.message.filter(AdminIdsFilter(config.tg_bot.admin_ids))


@admin_router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(
        text=f"Hello, {html.bold(message.from_user.full_name)}! You are admin",
        parse_mode=ParseMode.HTML,
        reply_markup=create_keyboard("button 1", "button 2")
    )


@admin_router.message(Command(commands='table'))
async def table(message: Message):
    create_table('textik', 228)
    await message.answer(text='Таблица создана')
