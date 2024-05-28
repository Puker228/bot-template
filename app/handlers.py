from aiogram import Router, F, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.enums import ParseMode

from config import load_config
from other.texts import lexicon
from .kb import create_keyboard

router = Router()
config = load_config()


@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(
        text=f"Hello, {html.bold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
        reply_markup=create_keyboard("button 1", "button 2")
    )


@router.message(Command(commands='remove'))
async def remove_kb(message: Message):
    await message.answer(text='229', reply_markup=ReplyKeyboardRemove())


@router.callback_query()
async def button_text(callback: CallbackQuery):
    await callback.message.answer(text=f"{callback.data}, puks")
