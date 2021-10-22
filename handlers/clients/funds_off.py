from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp

from utils.db_api.db import ClientsModel
from states.clients import Withdrawal
from .utils import correct_amount
from utils.notifications import notify_admin_about_withdrawal


@dp.message_handler(text="Вывод средств")
async def funds_off(message: types.Message):
    await message.answer("Информационный блок с % комиссии")
    await message.answer("Пришлите сумму")
    await Withdrawal.get_withdrawal_amount.set()


@dp.message_handler(state=Withdrawal.get_withdrawal_amount)
async def get_withdrawal_amount(message: types.Message, state: FSMContext):
    amount = message.text.replace(' ', '')
    client = ClientsModel.get_client_by_telegram_id(message.from_user.id)

    try:
        amount = int(amount)
        if amount > client.deposit:
            await message.answer(f"Сумма не должна превышать ваш депозит. На данный момент он составляет "
                                 f"{client.deposit} руб.")
        else:
            try:
                await notify_admin_about_withdrawal(client.telegram_id, amount)
                await message.answer("Запрос отправлен администратору. Ожидайте ответ")
            except ValueError:
                await message.answer("При отправке данных администратору возникла непредвиденная ошибка. "
                                     "Повторите попытку позже")
            await state.finish()
    except ValueError:
        await message.answer("Сумма должна быть указана целым числом")


