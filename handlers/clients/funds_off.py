from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp

from utils.db_api.db import ClientsModel
from states.clients import Withdrawal
from .utils import correct_amount


@dp.message_handler(text="Вывод средств")
async def funds_off(message: types.Message):
    await message.answer("Информационный блок с % комиссии")
    await message.answer("Пришлите сумму")
    await Withdrawal.get_withdrawal_amount.set()


@dp.message_handler(state=Withdrawal.get_withdrawal_amount)
async def get_withdrawal_amount(message: types.Message, state: FSMContext):
    amount = message.text
    client = ClientsModel.get_client_by_telegram_id(message.from_user.id)
    if correct_amount(amount, client.account):
        await message.answer("Запрос отправлен администратору. Ожидайте ответ")
        await state.finish()
    else:
        await message.answer("Указана неверная сумма")


