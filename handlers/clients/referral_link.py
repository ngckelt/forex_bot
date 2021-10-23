from aiogram import types
from loader import dp


@dp.message_handler(text="Реферальная ссылка")
async def start(message: types.Message):
    bot_name = (await message.bot.get_me()).username
    # link = f"https://t.me/{bot_name}?start={message.from_user.id}"
    link = f"https://t.me/{bot_name}?start=123123123"
    await message.answer(f"Вот ваша реферальная ссылка:\n{link}")



