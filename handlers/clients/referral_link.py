from aiogram import types
from loader import dp


from utils.db_api.db import ClientsModel


@dp.message_handler(text="Реферальная ссылка")
async def create_referral_link(message: types.Message):
    bot_name = (await message.bot.get_me()).username
    link = f"https://t.me/{bot_name}?start={message.from_user.id}"
    await message.answer(f"Вот ваша реферальная ссылка:\n{link}")

