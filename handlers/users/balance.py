from decimal import Decimal

from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.string import Buttons
from keyboards.inline.users.common import get_go_back_keyboard
from loader import dp
from states.balance import TopUP


@dp.callback_query_handler(text_contains=Buttons.TOP_UP_BALANCE.callback_data)
async def top_up_handler(callback: types.CallbackQuery, state: FSMContext):
    try:
        # await state.set_state(Contact.text)
        await callback.message.edit_text('Please, enter the amount: ',
                                         reply_markup=await get_go_back_keyboard(Buttons.BALANCE.callback_data))
        await TopUP.amount.set()
    except:
        ...


@dp.message_handler(state=TopUP.amount)
async def get_amount_handler(message: types.Message, state: FSMContext):
    try:
        amount = Decimal(message.text)
        if amount <= Decimal(0):
            raise ValueError()

        await state.finish()
    except (ValueError, TypeError):
        await message.reply('The amount must be a number and greater then 0')
