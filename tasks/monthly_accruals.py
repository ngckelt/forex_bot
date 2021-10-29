from pprint import pprint

from utils.db_api.db import ClientsModel, ReferralAccrualsModel, DepositsModel, WithdrawalsModel
from handlers.admins.utils import get_delta_days, get_current_month_number, get_month_days_quantity, TEN_PERCENT, \
    ONE_PERCENT, get_current_month_day
from datetime import datetime, timezone, timedelta
from utils.notifications import notify_referrer_about_month_deposit_update, notify_admin_about_month_deposit_update, \
    notify_client_about_month_deposit_update, notify_admin_about_one_percent_deposit_update
from data.config import DEFAULT_USERNAME

MONTH_DEPOSIT_UPDATE_DELTA_DAYS = 30


async def has_withdrawals(client):
    previous_month_number = get_current_month_number() - 1
    client_withdrawals = await WithdrawalsModel.get_client_withdrawals(client.telegram_id)
    for client_withdrawal in client_withdrawals:
        if int(client_withdrawal.datetime.strftime('%m')) == previous_month_number:
            return True
    return False


async def get_previous_month_deposit_updates(client):
    updates = list()
    previous_month_number = get_current_month_number() - 1
    deposit_updates = await DepositsModel.get_client_deposits(client.telegram_id)
    for deposit_update in deposit_updates:
        if int(deposit_update.datetime.strftime('%m')) == previous_month_number:
            updates.append(deposit_update)
    return updates


async def accrual_months_percents():
    # if get_current_month_day() != 1:
    #     return
    previous_month_number = get_current_month_number() - 1
    previous_month_days_quantity = get_month_days_quantity(previous_month_number)
    clients = await ClientsModel.get_clients()
    for client in clients:
        if not await has_withdrawals(client):
            previous_month_deposit_updates = await get_previous_month_deposit_updates(client)
            bonus = 0
            for deposit_update in previous_month_deposit_updates:
                delta_days = previous_month_days_quantity - int(deposit_update.datetime.strftime('%d')) + 1
                percent = delta_days / previous_month_days_quantity * TEN_PERCENT
                bonus += round(float(deposit_update.amount) * percent, 2)

            await ClientsModel.update_client(client.telegram_id, deposit=client.deposit + bonus)
            await notify_admin_about_month_deposit_update(client, bonus)
            await notify_client_about_month_deposit_update(client.telegram_id, bonus, client.deposit + bonus)
            if client.referer:
                referrer = await ClientsModel.get_client_by_telegram_id(client.referer)
                referer_bonus = round(client.deposit * ONE_PERCENT, 2)
                await ClientsModel.update_client(referrer.telegram_id, deposit=referrer.deposit + referer_bonus)
                await notify_referrer_about_month_deposit_update(referrer.telegram_id, client, referer_bonus)
                await notify_admin_about_one_percent_deposit_update(referrer, client.telegram_id,
                                                                    referer_bonus)
                await ReferralAccrualsModel.add_referral_accrual(
                    amount=referer_bonus,
                    accrual_to=referrer.username if referrer.username != DEFAULT_USERNAME else referrer.telegram_id,
                    accrual_from=client.username if client.username != DEFAULT_USERNAME else client.telegram_id,
                    datetime=datetime.now(timezone.utc)
                )



