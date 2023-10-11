from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from constants.string import Buttons


async def get_balance_menu_keyboard(go_to=Buttons.PROFILE.callback_data):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=Buttons.WITHDRAWAL_BALANCE.name,
                                 callback_data=Buttons.WITHDRAWAL_BALANCE.callback_data),
            InlineKeyboardButton(text=Buttons.TOP_UP_BALANCE.name,
                                 callback_data=Buttons.TOP_UP_BALANCE.callback_data),
        ],
        [InlineKeyboardButton(text=Buttons.GO_BACK.name, callback_data=go_to)]
    ])
