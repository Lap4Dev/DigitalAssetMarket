from aiogram.dispatcher.filters.state import StatesGroup, State


class TopUP(StatesGroup):
    type = State()
    amount = State()
