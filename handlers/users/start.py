from aiogram import types

from constants.string import BotCommand
from decorators.error_handler import async_error_handler
from handlers.users.main import show_main_menu_profile
from loader import dp, telegram_user_dal, wallet_dal


@dp.message_handler(commands=[BotCommand.START])
@async_error_handler
async def command_start_handler(message: types.Message):
    user_id, username = message.from_user.id, message.from_user.username
    user, user_was_created = await telegram_user_dal.create_user_if_not_exist(user_id=user_id, username=username)
    if user_was_created:
        await wallet_dal.create_wallet_by_user_if_not_exist(user)

    await show_main_menu_profile(message)

