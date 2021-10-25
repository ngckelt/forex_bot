from utils.db_api.db import ClientsModel
from .utils import send_message


async def notify_referrer_about_two_percent_deposit_update(referrer_telegram_id, referral_username, bonus):
    client = await ClientsModel.get_client_by_telegram_id(referrer_telegram_id)
    message = f"Вам был начислен бонус {bonus} руб. за пополнение пользователем {referral_username}. Ваш " \
              f"депозит на данный момент составляет: {client.deposit} руб."
    await send_message(referrer_telegram_id, message)


async def notify_referrer_about_one_percent_deposit_update(referrer_telegram_id, referral_username, bonus):
    client = await ClientsModel.get_client_by_telegram_id(referrer_telegram_id)
    message = f"Вам был начислен бонус {bonus} руб. за ежемесячное пополнение пользователя {referral_username}. Ваш " \
              f"депозит на данный момент составляет: {client.deposit} руб."
    await send_message(referrer_telegram_id, message)


