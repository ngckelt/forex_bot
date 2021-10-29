from utils.db_api.db import BotAdminsModel
from keyboards.inline.admin import confirm_update_deposit_markup, confirm_withdrawal_markup
from .utils import send_message_to_admin, get_user_contact


async def notify_admin_about_update_deposit(client, amount, deposit, commission):
    admin = await BotAdminsModel.get_active_bot_admin()
    text = f"Пользователь {get_user_contact(client)} хочет пополнить свой депозит.\n" \
           f"Сумма перевода: {amount} руб.\n" \
           f"Депозит: {deposit} руб.\n" \
           f"Комиссия: {commission} руб."
    await send_message_to_admin(admin, text, confirm_update_deposit_markup(client.telegram_id, amount))


async def notify_admin_about_withdrawal(client, amount, card_number, withdrawal_sum, commission):
    admin = await BotAdminsModel.get_active_bot_admin()
    text = f"Пользователь {get_user_contact(client)} хочет вывести со своего счета сумму {amount} руб.\n" \
           f"Номер карты: {card_number}\n" \
           f"Сумма вывода: {withdrawal_sum} руб.\n" \
           f"Комиссия: {commission} руб."
    await send_message_to_admin(admin, text, confirm_withdrawal_markup(client.telegram_id, amount))


async def notify_admin_about_one_percent_referral_deposit_update(referrer, referral, amount, bonus):
    admin = await BotAdminsModel.get_active_bot_admin()
    text = f"Пользователю {get_user_contact(referrer)} был начислен бонус 1% ({bonus} руб.) от суммы {amount} " \
           f"за пользователя {get_user_contact(referral)}"
    await send_message_to_admin(admin, text)


async def notify_admin_about_month_deposit_update(client, bonus):
    admin = await BotAdminsModel.get_active_bot_admin()
    text = f"Пользвателю {get_user_contact(client)} был начислен месячный бонус в размере {bonus} руб."
    await send_message_to_admin(admin, text)


async def notify_admin_about_one_percent_deposit_update(referrer, referral_telegram_id, bonus):
    admin = await BotAdminsModel.get_active_bot_admin()
    text = f"Пользователю {get_user_contact(referrer)} был начислен бонус ({bonus} руб.) " \
           f"за пользователя {referral_telegram_id} (месячное пополнение)"
    await send_message_to_admin(admin, text)


"""
При пополнении:
Когда чел отправляет 10тр
Ему приходит сообщение:
Депозит будет пополнен на 9000руб
Комиссия за пополнение составила 1000руб

Админу приходит: 
Пользователь Устюгов Игорь Константинович @igork76 хочет пополнить свой депозит.
Сумма перевода 10000руб
Депозит 9000руб
Комиссия 1000руб

При выводе:
Когда чел отправляет 10тр
Ему приходит сообщение:
Вы выводите 10тр
На карту получите 9000руб
Комиссия за вывод составит 1000руб

Админу приходит: 
Пользователь Устюгов Игорь Константинович @igork76 хочет вывести со своего счета сумму 10000 руб.
Номер карты: 1111 2222 5555 7777
Сумма вывода 9000руб
Комиссия 1000руб
"""
