from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from constants.string import Buttons


class YesNo(BoundFilter):
    async def check(self, callback: types.CallbackQuery) -> bool:
        return callback.data in [Buttons.YES.callback_data, Buttons.NO.callback_data]
