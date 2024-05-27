from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove

from config import load_config
from other.texts import lexicon
from .kb import create_keyboard

router = Router()
config = load_config()


@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(text=lexicon['/start'], reply_markup=create_keyboard("button 1", "button 2"))


@router.message(Command(commands='remove'))
async def remove_kb(message: Message):
    await message.answer(text='229', reply_markup=ReplyKeyboardRemove())
