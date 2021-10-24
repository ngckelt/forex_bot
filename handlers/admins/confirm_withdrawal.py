from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp

from utils.db_api.db import ClientsModel, WithdrawalsModel
from utils.notifications import notify_client_about_success_withdrawal, notify_client_about_failed_withdrawal
from filters.admin_filters import AdminOnly
from keyboards.inline.admin import confirm_withdrawal_callback
from states.admins import NotifyClients


@dp.callback_query_handler(AdminOnly(), confirm_withdrawal_callback.filter())
async def confirm_withdrawal(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.answer()
    choice = callback_data.get('choice')
    amount = callback_data.get('amount')
    client_telegram_id = callback_data.get('client_telegram_id')
    client = await ClientsModel.get_client_by_telegram_id(client_telegram_id)

    if choice == 'confirm':
        try:
            await WithdrawalsModel.add_withdrawal(
                telegram_id=client.telegram_id,
                username=client.username,
                first_name=client.first_name,
                last_name=client.last_name,
                middle_name=client.middle_name,
                amount=amount,
                card_number=client.card_number
            )
        except Exception as e:
            print(e)
            await callback.message.answer("Возникла непредвиденная ошибка")
            return
        await ClientsModel.update_client(client_telegram_id, deposit=client.deposit - int(amount))
        try:
            await notify_client_about_success_withdrawal(client_telegram_id, amount)
            await callback.message.answer("Сообщение успещно отправлено пользователю")
        except ValueError:
            await callback.message.answer(f"Не удалось отправить сообщение пользователю {client_telegram_id}. "
                                          f"Возможно, он удалил чат с ботом")
    else:
        await state.update_data(client_telegram_id=client_telegram_id, amount=amount)
        await NotifyClients.get_failed_withdrawal_reason.set()
        await callback.message.answer("Укажите причину отказа")


@dp.message_handler(AdminOnly(), state=NotifyClients.get_failed_withdrawal_reason)
async def get_failed_withdrawal_reason(message: types.Message, state: FSMContext):
    reason = message.text
    state_data = await state.get_data()
    try:
        await notify_client_about_failed_withdrawal(
            client_telegram_id=state_data.get('client_telegram_id'),
            amount=state_data.get('amount'),
            reason_text=reason
        )
        await message.answer("Сообщение успешно отправлено пользователю")
    except ValueError:
        await message.answer(f"Не удалось отправить сообщение пользователю {state_data.get('client_telegram_id')}. "
                             f"Возможно, он удалил чат с ботом")
    await state.finish()





