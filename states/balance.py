from aiogram.dispatcher.filters.state import StatesGroup, State


class TopUP(StatesGroup):
    amount = State()


class Withdraw(StatesGroup):
    amount = State()
    wallet = State()
    confirm_wallet = State()

