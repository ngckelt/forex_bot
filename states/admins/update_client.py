from aiogram.dispatcher.filters.state import StatesGroup, State


class UpdateClient(StatesGroup):
    get_amount = State()


