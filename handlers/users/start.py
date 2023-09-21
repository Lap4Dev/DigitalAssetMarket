from aiogram import types

from constants.string import BotCommand
from loader import dp


@dp.message_handler(commands=[BotCommand.START])
async def command_start_handler(message: types.Message):
    print(message.from_user.language_code)

