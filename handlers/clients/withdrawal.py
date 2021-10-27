from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp

from utils.db_api.db import ClientsModel
from states.clients import Withdrawal
from .utils import correct_amount, correct_card_number, split_card_number
from utils.notifications import notify_admin_about_withdrawal
from keyboards.inline import yes_or_no_markup, yes_or_no_callback


@dp.message_handler(text="Вывод средств")
async def funds_off(message: types.Message, state: FSMContext):
    client = await ClientsModel.get_client_by_telegram_id(message.from_user.id)
    if client.deposit == 0:
        await message.answer("Ваш депозит составляет 0.0 руб. Вы не можете осуществить вывод средств")
        return
    await message.answer("Информационный блок с % комиссии")
    await message.answer(f"Ваш депозит на данный момент составляет {client.deposit} руб.")
    await state.update_data(card_number=client.card_number)
    await message.answer(
        f"Использовать эту карту: {client.card_number}?",
        reply_markup=yes_or_no_markup('use_existing_card_for_withdrawal')
    )
    await Withdrawal.use_existing_card.set()


@dp.callback_query_handler(yes_or_no_callback.filter(question="use_existing_card_for_withdrawal"),
                           state=Withdrawal.use_existing_card)
async def use_existing_card(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.answer()
    choice = callback_data.get('choice')
    if choice == 'yes':
        await callback.message.answer("Пришлите сумму")
        await Withdrawal.get_withdrawal_amount.set()
    else:
        await callback.message.answer("Пришлите новый номер карты")
        await Withdrawal.get_new_card_number.set()


@dp.message_handler(state=Withdrawal.get_new_card_number)
async def get_new_card_number(message: types.Message, state: FSMContext):
    card_number = message.text
    if correct_card_number(card_number):
        card_number = split_card_number(card_number)
        await state.update_data(card_number=card_number)
        await ClientsModel.update_client(message.from_user.id, card_number=card_number)
        await message.answer("Пришлите сумму")
        await Withdrawal.get_withdrawal_amount.set()
    else:
        await message.answer("Неверный формат номера карты")


@dp.message_handler(state=Withdrawal.get_withdrawal_amount)
async def get_withdrawal_amount(message: types.Message, state: FSMContext):
    amount = message.text.replace(' ', '')
    client = await ClientsModel.get_client_by_telegram_id(message.from_user.id)

    try:
        amount = int(amount)
        if amount > client.deposit:
            await message.answer(f"Сумма не должна превышать ваш депозит. На данный момент он составляет "
                                 f"{client.deposit} руб.")
        else:
            try:
                await notify_admin_about_withdrawal(client.telegram_id, amount, client.card_number)
                await message.answer("Запрос отправлен администратору. Ожидайте ответ")
            except ValueError:
                await message.answer("При отправке данных администратору возникла непредвиденная ошибка. "
                                     "Повторите попытку позже")
            await state.finish()
    except ValueError:
        await message.answer("Сумма должна быть указана целым числом")


