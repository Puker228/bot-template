from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_keyboard(text_first, text_second) -> InlineKeyboardMarkup:
    yes_button = InlineKeyboardButton(text=text_first, callback_data='yes')
    no_button = InlineKeyboardButton(text=text_second, callback_data="no")
    keyboard: list[list[InlineKeyboardButton]] = [[yes_button, no_button]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
