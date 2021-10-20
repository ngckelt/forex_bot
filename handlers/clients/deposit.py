from aiogram import types
from loader import dp

from utils.db_api.db import ClientsModel


@dp.message_handler(text="Депозит")
async def show_deposit(message: types.Message):
    client = ClientsModel.get_client_by_telegram_id(message.from_user.id)
    await message.answer(f"Ваш депозит на данный момент: {client.account}р.")

