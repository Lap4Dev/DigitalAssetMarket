from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from constants.string import Buttons


async def get_profile_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=Buttons.BALANCE.name, callback_data=Buttons.BALANCE.callback_data),
            InlineKeyboardButton(text=Buttons.MY_PRODUCTS.name, callback_data=Buttons.MY_PRODUCTS.callback_data)
        ],
        [InlineKeyboardButton(text=Buttons.GO_BACK.name, callback_data=Buttons.MAIN_MENU.callback_data)]
    ])
