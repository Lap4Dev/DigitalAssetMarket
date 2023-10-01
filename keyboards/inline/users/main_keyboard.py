from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from constants.string import Buttons


async def get_main_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=Buttons.PROFILE.name, callback_data=Buttons.PROFILE.callback_data)],
        [InlineKeyboardButton(text=Buttons.HELP.name, callback_data=Buttons.HELP.callback_data)]
    ])
