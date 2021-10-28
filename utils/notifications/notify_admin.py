from utils.db_api.db import BotAdminsModel
from keyboards.inline.admin import confirm_update_deposit_markup, confirm_withdrawal_markup
from .utils import send_message_to_admin, get_user_contact


async def notify_admin_about_update_deposit(client, amount, card_number):
    admin = await BotAdminsModel.get_active_bot_admin()
    text = f"Пользователь {get_user_contact(client)} хочет пополнить свой депозит на сумму {amount} руб.\nНомер карты: " \
           f"{card_number}"
    await send_message_to_admin(admin, text, confirm_update_deposit_markup(client.telegram_id, amount))


async def notify_admin_about_withdrawal(client, amount, card_number):
    admin = await BotAdminsModel.get_active_bot_admin()
    text = f"Пользователь {get_user_contact(client)} хочет вывести со своего счета сумму {amount} руб.\nНомер карты: " \
           f"{card_number}"
    await send_message_to_admin(admin, text, confirm_withdrawal_markup(client.telegram_id, amount))


async def notify_admin_about_two_percent_deposit_update(referrer, referral, amount, bonus):
    admin = await BotAdminsModel.get_active_bot_admin()
    text = f"Пользователю {get_user_contact(referrer)} был начислен бонус 2% ({bonus} руб.) от суммы {amount} " \
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


