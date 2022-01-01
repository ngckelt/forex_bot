from .utils import send_message_to_client
from utils.db_api.db import ClientsModel
from handlers.admins.utils import TEN_PERCENT


async def notify_client_about_success_deposit_update(client_telegram_id, amount):
    amount = round(float(amount), 2)
    client = await ClientsModel.get_client_by_telegram_id(client_telegram_id)
    text = f"Вам зачислено {amount} руб. Ваш депозит на данный момент составляет " \
           f"{round(client.deposit, 2)} руб."
    await send_message_to_client(client_telegram_id, text)


async def notify_client_about_failed_deposit_update(client_telegram_id, amount, reason_text):
    amount = round(float(amount), 2)
    text = f"Ваш запрос на пополнение {amount} руб. не принят\nПричина: {reason_text}"
    await send_message_to_client(client_telegram_id, text)


async def notify_client_about_success_withdrawal(client_telegram_id, amount):
    amount = round(float(amount), 2)
    client = await ClientsModel.get_client_by_telegram_id(client_telegram_id)
    text = f"Ваш запрос на вывод {amount} руб. принят. Ваш депозит на данный момент составляет {client.deposit} руб."
    await send_message_to_client(client_telegram_id, text)


async def notify_client_about_failed_withdrawal(client_telegram_id, amount, reason_text):
    amount = round(float(amount), 2)
    text = f"Ваш запрос на вывод {amount} руб. не принят\nПричина: {reason_text}"
    await send_message_to_client(client_telegram_id, text)


async def notify_client_about_month_deposit_update(client_telegram_id, bonus, new_deposit):
    bonus = round(float(bonus), 2)
    text = f"Вам был начислен месячный бонус в размере {bonus} руб. Ваш текущий депозит составляет " \
           f"{round(new_deposit, 2)} руб."
    await send_message_to_client(client_telegram_id, text)



