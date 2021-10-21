from aiogram.dispatcher.filters.state import StatesGroup, State


class NotifyClients(StatesGroup):
    get_text = State()
    ask_photo = State()
    get_photo = State()
    confirm = State()


