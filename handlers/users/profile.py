from aiogram import types

from constants.string import Buttons, Messages
from decorators.error_handler import async_error_handler
from keyboards.inline.users.profile_keyboard import get_profile_kb
from loader import dp
from telegram_models.profile import TelegramProfile


@async_error_handler
async def show_inline_user_profile(call: types.CallbackQuery, profile_info: TelegramProfile):
    await call.message.edit_text(
        text=Messages.get_profile_message(profile_info),
        reply_markup=await get_profile_kb()
    )


@dp.callback_query_handler(text_contains=Buttons.PROFILE.callback_data)
@async_error_handler
async def profile_handler(callback: types.CallbackQuery):
    await show_inline_user_profile(callback, TelegramProfile(callback.from_user.id, callback.from_user.first_name))
