from aiogram import types

from constants.string import Buttons, Messages
from decorators.error_handler import async_error_handler
from keyboards.inline.users.common import get_go_back_keyboard
from loader import dp


async def show_care_service(callback: types.CallbackQuery):
    await callback.message.edit_text(Messages.CARE_SERVICE_MESSAGE,
                                     reply_markup=await get_go_back_keyboard(Buttons.MAIN_MENU.callback_data))


@dp.callback_query_handler(text_contains=Buttons.HELP.callback_data)
@async_error_handler
async def command_start_handler(callback: types.CallbackQuery):
    await show_care_service(callback)


