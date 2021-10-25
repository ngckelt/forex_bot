from utils.db_api.db import ClientsModel, ReferralAccrualsModel
from handlers.admins.utils import get_delta_days
from datetime import datetime, timezone
from utils.notifications import notify_client_about_ten_percent_deposit_update, \
    notify_admin_about_ten_percent_deposit_update, notify_referrer_about_one_percent_deposit_update, \
    notify_admin_about_one_percent_deposit_update
from .utils import count_bonus, count_referrer_bonus

MONTH_DEPOSIT_UPDATE_DELTA_DAYS = 30


async def accrual_ten_percent():
    now = datetime.now(timezone.utc)
    clients = await ClientsModel.get_clients()
    for client in clients:
        dd = get_delta_days(now, client.last_update_deposit_date)
        print(dd)
        if get_delta_days(now, client.last_update_deposit_date) == MONTH_DEPOSIT_UPDATE_DELTA_DAYS:
            bonus = count_bonus(client.deposit)
            await ClientsModel.update_client(client.telegram_id, deposit=client.deposit + bonus)
            await notify_client_about_ten_percent_deposit_update(client.telegram_id, bonus, client.deposit + bonus)
            await notify_admin_about_ten_percent_deposit_update(client.telegram_id, bonus)

            if client.referer:
                referrer = await ClientsModel.get_client_by_telegram_id(client.referer)
                referrer_bonus = count_referrer_bonus(bonus)
                await ClientsModel.update_client(referrer.telegram_id, deposit=referrer.deposit + referrer_bonus)
                await notify_referrer_about_one_percent_deposit_update(referrer.telegram_id, client.telegram_id,
                                                                       referrer_bonus)
                await notify_admin_about_one_percent_deposit_update(referrer.telegram_id, client.telegram_id, bonus,
                                                                    referrer_bonus)
                await ReferralAccrualsModel.add_referral_accrual(
                    amount=referrer_bonus,
                    accrual_to=referrer.telegram_id,
                    accrual_from=client.telegram_id,
                    datetime=now,
                )





