from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from constants.string import Buttons


async def get_go_back_keyboard(go_to=Buttons.MAIN_MENU.callback_data):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=Buttons.GO_BACK.name, callback_data=go_to)]
    ])
