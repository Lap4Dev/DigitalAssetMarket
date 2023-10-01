from aiogram import types

from constants.string import Buttons, Messages
from dashboard.marketplace.dals.telegram_user_dal import ShowUserSchema
from decorators.error_handler import async_error_handler
from keyboards.inline.users.profile_keyboard import get_profile_kb
from loader import dp, telegram_user_dal


@async_error_handler
async def show_inline_user_profile(call: types.CallbackQuery, profile_info: ShowUserSchema):
    await call.message.edit_text(
        text=Messages.get_profile_message(profile_info),
        reply_markup=await get_profile_kb()
    )


@dp.callback_query_handler(text_contains=Buttons.PROFILE.callback_data)
@async_error_handler
async def profile_handler(callback: types.CallbackQuery):
    user_info = await telegram_user_dal.get_user_profile_info_by_id(callback.from_user.id)
    await show_inline_user_profile(callback, user_info)
