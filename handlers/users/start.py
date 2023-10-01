from aiogram import types

from constants.string import BotCommand
from decorators.error_handler import async_error_handler
from handlers.users.main import show_main_menu_profile
from loader import dp, telegram_user_dal


@dp.message_handler(commands=[BotCommand.START])
@async_error_handler
async def command_start_handler(message: types.Message):
    user_id, username = message.from_user.id, message.from_user.username
    await telegram_user_dal.create_user_if_not_exist(user_id=user_id, username=username)
    await show_main_menu_profile(message)
