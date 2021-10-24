from aiogram.dispatcher.filters.state import StatesGroup, State


class Withdrawal(StatesGroup):
    get_withdrawal_amount = State()
    use_existing_card = State()
    get_new_card_number = State()

