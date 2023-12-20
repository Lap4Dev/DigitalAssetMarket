from decimal import Decimal

from aiogram import types
from aiogram.dispatcher import FSMContext

from constants.string import Buttons, Messages
from dashboard.marketplace.dals.withdraw_dal import WithdrawDAL
from data import config
from decorators.error_handler import async_error_handler
from filters.basic_callback import YesNo
from filters.basic_message import IsValidAmount
from keyboards.inline.users.balance import get_balance_menu_keyboard
from keyboards.inline.users.common import get_go_back_keyboard, yes_no_keyboard
from loader import dp, telegram_user_dal
from notification.admin import notify_withdraw_request
from states.balance import TopUP, Withdraw
from utils.disappearing_message import disappearing_message


@async_error_handler
async def show_inline_balance_menu(callback: types.CallbackQuery, balance: float = 0):
    username, chat_id = callback.from_user.username, callback.from_user.id

    await callback.message.edit_text(Messages.get_balance_message(
        balance, username, chat_id
    ), reply_markup=await get_balance_menu_keyboard())


@dp.callback_query_handler(text_contains=Buttons.BALANCE.callback_data, state='*')
@async_error_handler
async def balance_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    balance = await telegram_user_dal.get_user_balance_by_id(callback.from_user.id)
    await show_inline_balance_menu(callback, balance or 0)


@dp.callback_query_handler(text_contains=Buttons.TOP_UP_BALANCE.callback_data)
@async_error_handler
async def top_up_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        Messages.POP_UP_BALANCE,
        reply_markup=await get_go_back_keyboard(Buttons.BALANCE.callback_data)
    )
    await TopUP.amount.set()


@dp.message_handler(IsValidAmount(), state=TopUP.amount, content_types=types.ContentType.TEXT)
async def get_amount_handler(message: types.Message, state: FSMContext):
    await state.finish()
    amount = message.text


@dp.callback_query_handler(text_contains=Buttons.WITHDRAWAL_BALANCE.callback_data)
@async_error_handler
async def withdraw_balance_handler(callback: types.CallbackQuery):
    balance = await telegram_user_dal.get_user_balance_by_id(callback.from_user.id)

    await callback.message.edit_text(
        Messages.PRE_WITHDRAW(balance or 0),
        reply_markup=await get_go_back_keyboard(Buttons.BALANCE.callback_data)
    )
    await Withdraw.amount.set()


@dp.message_handler(IsValidAmount(), state=Withdraw.amount, content_types=types.ContentType.TEXT)
@async_error_handler
async def get_amount_handler(message: types.Message, state: FSMContext):
    balance = await telegram_user_dal.get_user_balance_by_id(message.from_user.id)
    amount = float(message.text)
    if amount > balance:
        return await disappearing_message(message, Messages.AMOUNT_MUST_BE_LOWER_THEN_BALANCE)

    async with state.proxy() as data:
        data['amount'] = amount

    await message.answer(
        Messages.ENTER_USDT_WALLET,
        reply_markup=await get_go_back_keyboard(Buttons.BALANCE.callback_data)
    )

    await Withdraw.wallet.set()


@dp.message_handler(state=Withdraw.wallet, content_types=types.ContentType.TEXT)
@async_error_handler
async def get_withdraw_wallet_handler(message: types.Message, state: FSMContext):
    wallet = message.text

    await message.answer(
        Messages.VALID_WALLET_ADDRESS(wallet),
        reply_markup=yes_no_keyboard()
    )
    async with state.proxy() as data:
        data['wallet'] = wallet

    await Withdraw.confirm_wallet.set()


@dp.callback_query_handler(YesNo(), state=Withdraw.confirm_wallet)
@async_error_handler
async def confirming_withdrawal_address(callback: types.CallbackQuery, state: FSMContext):
    decision = callback.data

    if decision == Buttons.NO.callback_data:
        await callback.message.edit_text(
            Messages.ENTER_USDT_WALLET,
            reply_markup=await get_go_back_keyboard(Buttons.BALANCE.callback_data)
        )

        return await Withdraw.wallet.set()

    async with state.proxy() as data:
        amount = data.get('amount')
        wallet = data.get('wallet')

    balance = await telegram_user_dal.get_user_balance_by_id(callback.from_user.id)

    if amount > balance:
        await callback.message.edit_text(
            Messages.PRE_WITHDRAW(balance or 0),
            reply_markup=await get_go_back_keyboard(Buttons.BALANCE.callback_data)
        )
        await Withdraw.amount.set()

    user_id = callback.from_user.id
    withdraw_request = await WithdrawDAL().make_withdraw_request(
        user_id=callback.from_user.id,
        withdraw_amount=amount,
        withdraw_address=wallet
    )
    if withdraw_request is None:
        await callback.message.edit_text(
            Messages.ERROR_OCCURRED,
            reply_markup=await get_go_back_keyboard(Buttons.BALANCE.callback_data)
        )
        return await state.finish()

    was_balance_set = await telegram_user_dal.set_user_balance(user_id, Decimal(balance - amount))
    if not was_balance_set:
        await callback.message.edit_text(
            Messages.ERROR_OCCURRED,
            reply_markup=await get_go_back_keyboard(Buttons.BALANCE.callback_data)
        )
        return await state.finish()

    msg_kwargs = dict(
        request_id=withdraw_request.id,
        user_id=user_id,
        username=callback.from_user.username,
        withdraw_amount=amount,
        withdraw_address=wallet,
        commission=config.WITHDRAW_FEE_AMOUNT * amount / 100
    )
    await notify_withdraw_request(**msg_kwargs)
    await callback.message.edit_text(
        Messages.WITHDRAW_REQUEST_SUBMITTED + f'\n\n{Messages.withdraw_request_notification(**msg_kwargs)}'
    )

    await state.finish()

