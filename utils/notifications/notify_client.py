from .utils import send_message


async def notify_client_about_success_deposit_update(client_telegram_id, amount):
    text = f"Ваш запрос на пополнение {amount} руб. принят"
    await send_message(client_telegram_id, text)


async def notify_client_about_failed_deposit_update(client_telegram_id, amount, reason_text):
    text = f"Ваш запрос на пополнение {amount} руб. не принят\nПричина: {reason_text}"
    await send_message(client_telegram_id, text)


async def notify_client_about_success_withdrawal(client_telegram_id, amount):
    text = f"Ваш запрос на вывод {amount} руб. принят"
    await send_message(client_telegram_id, text)


async def notify_client_about_failed_withdrawal(client_telegram_id, amount, reason_text):
    text = f"Ваш запрос на пополнение {amount} руб. не принят\nПричина: {reason_text}"
    await send_message(client_telegram_id, text)




