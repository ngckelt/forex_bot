from aiogram import types
from loader import dp


from utils.db_api.db import ClientsModel


@dp.message_handler(text="Реферальная ссылка")
async def create_referral_link(message: types.Message):

    # client = await ClientsModel.get_client_by_telegram_id(message.from_user.id)
    # referrals = await ClientsModel.get_referrals(client)
    #
    # print(referrals)

    bot_name = (await message.bot.get_me()).username
    # link = f"https://t.me/{bot_name}?start={message.from_user.id}"
    link = f"https://t.me/{bot_name}?start={message.from_user.id}"
    await message.answer(f"Вот ваша реферальная ссылка:\n{link}")

