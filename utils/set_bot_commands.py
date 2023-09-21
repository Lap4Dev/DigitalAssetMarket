from aiogram import Dispatcher, types

from constants import helper
from constants.string import BotCommand


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand(BotCommand.START, helper.COMMAND_START_HELPER),
        types.BotCommand(BotCommand.HELP, helper.COMMAND_HELP_HELPER),
    ])
