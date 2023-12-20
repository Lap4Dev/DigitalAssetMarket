from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from constants.string import Messages
from utils.disappearing_message import disappearing_message


class IsNumber(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        try:
            float(message.text)
            return True
        except ValueError:
            await disappearing_message(message, Messages.INVALID_AMOUNT)
            return False


class IsValidAmount(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        try:
            if float(message.text) <= 0:
                raise ValueError()

            return True
        except ValueError:
            await disappearing_message(message, Messages.INVALID_AMOUNT)
            return False
