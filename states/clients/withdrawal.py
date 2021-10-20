from aiogram.dispatcher.filters.state import StatesGroup, State


class Withdrawal(StatesGroup):
    get_withdrawal_amount = State()

