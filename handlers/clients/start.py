from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp

from keyboards.default.clients import main_markup
from utils.db_api.db import ClientsModel


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(
        text="Тут будет общая информация о владельце бота и услугах которые предоставляет.",
        reply_markup=main_markup
    )

    # ClientsModel.add_client(
    #     message.from_user.id,
    # )


