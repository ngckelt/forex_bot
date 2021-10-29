from utils.db_api.db import ClientsModel
from .utils import send_message_to_referrer, get_user_contact


async def notify_referrer_about_one_percent_deposit_update(referrer_telegram_id, referral, bonus):
    client = await ClientsModel.get_client_by_telegram_id(referrer_telegram_id)
    message = f"Вам был начислен бонус {bonus} руб. за пополнение пользователем {get_user_contact(referral)}. Ваш " \
              f"депозит на данный момент составляет: {client.deposit} руб."
    await send_message_to_referrer(referrer_telegram_id, message)


async def notify_referrer_about_month_deposit_update(referrer_telegram_id, referral, bonus):
    client = await ClientsModel.get_client_by_telegram_id(referrer_telegram_id)
    message = f"Вам был начислен бонус {bonus} руб. за ежемесячное пополнение пользователя " \
              f"{get_user_contact(referral)}. Ваш депозит на данный момент составляет: {client.deposit} руб."
    await send_message_to_referrer(referrer_telegram_id, message)


