from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from keyboards.inline.clients import confirm_markup, confirm_callback, back_to_confirm_markup, back_to_confirm_callback
from states.clients import UpdateDeposit
from .utils import correct_update_amount
from utils.notifications import notify_admin_about_update_deposit


@dp.message_handler(text="Пополнить счет")
async def update_deposit(message: types.Message):
    await message.answer(
        text="Информационный блок, об условиях, пополнения, вывода, получения прибыли",
        reply_markup=confirm_markup()
    )


@dp.callback_query_handler(confirm_callback.filter())
async def confirm_callback(callback: types.CallbackQuery, callback_data: dict):
    await callback.answer()
    choice = callback_data.get('choice')

    if choice == "True":
        await callback.message.answer("Пришлите сумму")
        await UpdateDeposit.get_amount.set()
    else:
        await callback.message.edit_text(
            text="Информационный блок, что счет нельзя пополнить не подписав согласие",
            reply_markup=back_to_confirm_markup()
        )


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
        try:
            await notify_admin_about_update_deposit(message.from_user.id, amount)
            await message.answer("Заявка отправлена администратору. Ожидайте ответ")
        except ValueError:
            await message.answer("При отправке данных администратору возникла непредвиденная ошибка. "
                                 "Повторите попытку позже")
        await state.finish()
    else:
        await message.answer("Сумма указана неверно")






