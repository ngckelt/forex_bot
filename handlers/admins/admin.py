from aiogram import types
from loader import dp

from utils.db_api.db import ClientsModel
from filters.admin_filters import AdminOnly


@dp.message_handler(AdminOnly(), text="test")
async def admin_test(message: types.Message):
    await message.answer("Фильтр прошел")

