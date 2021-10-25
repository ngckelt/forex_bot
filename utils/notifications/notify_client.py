from .utils import send_message
from utils.db_api.db import ClientsModel


async def notify_client_about_success_deposit_update(client_telegram_id, amount):
    client = await ClientsModel.get_client_by_telegram_id(client_telegram_id)
    text = f"Ваш запрос на пополнение {amount} руб. принят. Ваш депозит на данный момент составляет " \
           f"{client.deposit} руб."
    await send_message(client_telegram_id, text)


async def notify_client_about_failed_deposit_update(client_telegram_id, amount, reason_text):
    text = f"Ваш запрос на пополнение {amount} руб. не принят\nПричина: {reason_text}"
    await send_message(client_telegram_id, text)


async def notify_client_about_success_withdrawal(client_telegram_id, amount):
    client = await ClientsModel.get_client_by_telegram_id(client_telegram_id)
    text = f"Ваш запрос на вывод {amount} руб. принят. Ваш депозит на данный момент составляет {client.deposit} руб."
    await send_message(client_telegram_id, text)


async def notify_client_about_failed_withdrawal(client_telegram_id, amount, reason_text):
    text = f"Ваш запрос на вывод {amount} руб. не принят\nПричина: {reason_text}"
    await send_message(client_telegram_id, text)


async def notify_client_about_ten_percent_deposit_update(client_telegram_id, bonus, new_deposit):
    text = f"Вам был начислен месячный бонус в размере {bonus} руб. Ваш текущий депозит составляет {new_deposit} руб."
    await send_message(client_telegram_id, text)



