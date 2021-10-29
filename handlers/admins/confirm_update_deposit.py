from datetime import datetime, timezone

from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp

from utils.db_api.db import ClientsModel, DepositsModel, ReferralAccrualsModel
from utils.notifications import notify_client_about_success_deposit_update, notify_client_about_failed_deposit_update, \
    notify_referrer_about_one_percent_deposit_update, notify_admin_about_one_percent_referral_deposit_update
from filters.admin_filters import AdminOnly
from keyboards.inline.admin import confirm_update_deposit_callback
from states.admins import NotifyClients
from .utils import count_deposit, count_referrer_one_percent_deposit_update
from data.config import DEFAULT_USERNAME


@dp.callback_query_handler(AdminOnly(), confirm_update_deposit_callback.filter())
async def confirm_update_deposit(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.answer()
    choice = callback_data.get('choice')
    amount = callback_data.get('amount')
    client_telegram_id = callback_data.get('client_telegram_id')
    client = await ClientsModel.get_client_by_telegram_id(client_telegram_id)

    if choice == 'confirm':
        try:
            await DepositsModel.add_deposit(
                telegram_id=client.telegram_id,
                username=client.username,
                first_name=client.first_name,
                last_name=client.last_name,
                middle_name=client.middle_name,
                amount=amount,
                card_number=client.card_number
            )
        except:
            await callback.message.answer("При добавлении данных возникла непредвиденная ошибка")
            return
        deposit = count_deposit(client.deposit, int(amount), client.last_update_deposit_date)
        await ClientsModel.update_client(client_telegram_id, deposit=deposit)
        try:
            await notify_client_about_success_deposit_update(client_telegram_id, amount)
            await callback.message.answer("Сообщение успешно отправлено пользователю")
        except ValueError:
            await callback.message.answer(f"Не удалось отправить сообщение пользователю {client_telegram_id}. "
                                          f"Возможно, он удалил чат с ботом")

        if client.referer:
            bonus = count_referrer_one_percent_deposit_update(int(amount))
            referrer = await ClientsModel.get_client_by_telegram_id(client.referer)
            await ClientsModel.update_client(referrer.telegram_id, deposit=referrer.deposit + bonus)
            await notify_referrer_about_one_percent_deposit_update(referrer.telegram_id, client, bonus)
            await notify_admin_about_one_percent_referral_deposit_update(referrer, client, amount, bonus)
            await ReferralAccrualsModel.add_referral_accrual(
                amount=bonus,
                accrual_to=referrer.username if referrer.username != DEFAULT_USERNAME else referrer.telegram_id,
                accrual_from=client.username if client.username != DEFAULT_USERNAME else client.telegram_id,
                datetime=datetime.now(timezone.utc)
            )

    else:
        await state.update_data(client_telegram_id=client_telegram_id, amount=amount)
        await NotifyClients.get_failed_deposit_update_reason.set()
        await callback.message.answer("Укажите причину отказа")


@dp.message_handler(AdminOnly(), state=NotifyClients.get_failed_deposit_update_reason)
async def get_failed_deposit_update_reason(message: types.Message, state: FSMContext):
    reason = message.text
    state_data = await state.get_data()
    try:
        await notify_client_about_failed_deposit_update(
            client_telegram_id=state_data.get('client_telegram_id'),
            amount=state_data.get('amount'),
            reason_text=reason
        )
        await message.answer("Сообщение успешно отправлено пользователю")
    except ValueError:
        await message.answer(f"Не удалось отправить сообщение пользователю {state_data.get('client_telegram_id')}. "
                             f"Возможно, он удалил чат с ботом")
    await state.finish()
















