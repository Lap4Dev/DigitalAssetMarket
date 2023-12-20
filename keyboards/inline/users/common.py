from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from constants.string import Buttons


async def get_go_back_keyboard(go_to=Buttons.MAIN_MENU.callback_data):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=Buttons.GO_BACK.name, callback_data=go_to)]
    ])


def yes_no_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=Buttons.YES.name, callback_data=Buttons.YES.callback_data),
         InlineKeyboardButton(text=Buttons.NO.name, callback_data=Buttons.NO.callback_data), ]
    ])
