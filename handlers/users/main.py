from aiogram import types

from constants.string import Messages, Buttons
from decorators.error_handler import async_error_handler
from keyboards.inline.users.main_keyboard import get_main_menu_kb
from loader import dp


async def show_main_menu_profile(msg: types.Message, replace_old=False):
    if replace_old:
        return await msg.edit_text(Messages.WELCOME_MESSAGE, reply_markup=await get_main_menu_kb())

    await msg.answer(Messages.WELCOME_MESSAGE, reply_markup=await get_main_menu_kb())


@dp.callback_query_handler(text_contains=Buttons.MAIN_MENU.callback_data)
@async_error_handler
async def command_start_handler(callback: types.CallbackQuery):
    await show_main_menu_profile(callback.message, replace_old=True)
