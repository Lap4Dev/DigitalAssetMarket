import asyncio

from aiogram import types

from decorators.error_handler import async_error_handler
from loader import dp, _
from constants import messages


@dp.message_handler()
@async_error_handler
async def action_not_found_error(message: types.Message):
    error_message = await message.answer(_(messages.ACTION_NOT_FOUND_ERROR))
    await asyncio.sleep(3)
    await message.delete()
    await error_message.delete()

