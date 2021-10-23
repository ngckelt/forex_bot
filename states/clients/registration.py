from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterClient(StatesGroup):
    get_full_name = State()
    get_card_number = State()


