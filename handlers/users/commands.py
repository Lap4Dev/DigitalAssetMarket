from aiogram import types
from constants.string import BotCommand
from decorators.error_handler import async_error_handler
from loader import dp


@dp.message_handler(commands=[BotCommand.HELP])
@async_error_handler
async def command_help_handler(message: types.Message):
    await message.answer('/start - Start bot\n'
                         '/balance - Get balance menu\n'
                         '/products - Get products menu\n'
                         '/help - Get help')
