from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from datetime import datetime
from keyboards.default.clients import main_markup
from utils.db_api.db import ClientsModel


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    referer_telegram_id = message.get_args()
    if referer_telegram_id:
        referer = await ClientsModel.get_client_by_telegram_id(referer_telegram_id)
    await message.answer(
        text="Тут будет общая информация о владельце бота и услугах которые предоставляет.",
        reply_markup=main_markup
    )

    await ClientsModel.add_client(
        message.from_user.id,
        username=message.from_user.username,
        last_update_deposit_date=datetime.now()
    )

