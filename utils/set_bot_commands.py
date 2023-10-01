from aiogram import Dispatcher, types

from constants.string import BotCommand, Helper


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand(BotCommand.START, Helper.COMMAND_START_HELPER),
        types.BotCommand(BotCommand.HELP, Helper.COMMAND_HELP_HELPER),
    ])
