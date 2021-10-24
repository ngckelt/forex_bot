from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp

from keyboards.inline.clients import confirm_markup, confirm_callback, back_to_confirm_markup, back_to_confirm_callback
from keyboards.inline import yes_or_no_markup, yes_or_no_callback
from states.clients import UpdateDeposit
from .utils import correct_update_amount, correct_card_number, split_card_number
from utils.notifications import notify_admin_about_update_deposit
from utils.db_api.db import ClientsModel


@dp.message_handler(text="Пополнить счет")
async def update_deposit(message: types.Message):
    await message.answer(
        text="Информационный блок, об условиях, пополнения, вывода, получения прибыли",
        reply_markup=confirm_markup()
    )


@dp.callback_query_handler(confirm_callback.filter())
async def confirm_callback(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.answer()
    choice = callback_data.get('choice')

    if choice == "True":
        client = await ClientsModel.get_client_by_telegram_id(callback.from_user.id)
        await state.update_data(card_number=client.card_number)
        await callback.message.answer(
            text=f"Использовать эту карту: {client.card_number}?",
            reply_markup=yes_or_no_markup('use_existing_card')
        )
        await UpdateDeposit.use_existing_card.set()
    else:
        await callback.message.edit_text(
            text="Информационный блок, что счет нельзя пополнить не подписав согласие",
            reply_markup=back_to_confirm_markup()
        )


@dp.callback_query_handler(yes_or_no_callback.filter(question='use_existing_card'),
                           state=UpdateDeposit.use_existing_card)
async def use_existing_card(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.answer()
    choice = callback_data.get('choice')
    if choice == 'yes':
        await callback.message.answer("Пришлите сумму")
        await UpdateDeposit.get_amount.set()
    else:
        await callback.message.answer("Пришлите номер карты")
        await UpdateDeposit.get_new_card_number.set()


@dp.message_handler(state=UpdateDeposit.get_new_card_number)
async def get_new_card_number(message: types.Message, state: FSMContext):
    card_number = message.text
    if correct_card_number(card_number):
        card_number = split_card_number(card_number)
        await state.update_data(card_number=card_number)
        await ClientsModel.update_client(message.from_user.id, card_number=card_number)
        await message.answer("Пришлите сумму")
        await UpdateDeposit.get_amount.set()
    else:
        await message.answer("Неверный формат номера карты")


@dp.callback_query_handler(back_to_confirm_callback.filter())
async def back_to_confirm(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text="Информационный блок, об условиях, пополнения, вывода, получения прибыли",
        reply_markup=confirm_markup()
    )


@dp.message_handler(state=UpdateDeposit.get_amount)
async def get_amount(message: types.Message, state: FSMContext):
    amount = message.text.replace(' ', '')
    if correct_update_amount(amount):
        state_data = await state.get_data()
        card_number = state_data.get('card_number')
        try:
            await notify_admin_about_update_deposit(message.from_user.id, amount, card_number)
            await message.answer("Заявка отправлена администратору. Ожидайте ответ")
        except ValueError:
            await message.answer("При отправке данных администратору возникла непредвиденная ошибка. "
                                 "Повторите попытку позже")
        await state.finish()
    else:
        await message.answer("Сумма указана неверно")






