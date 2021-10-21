from utils.db_api.db import BotAdminsModel
from keyboards.inline.admin import confirm_update_deposit_markup, confirm_withdrawal_markup
from .utils import send_message


async def notify_admin_about_update_deposit(client_telegram_id, amount):
    admin = BotAdminsModel.get_active_bot_admin()
    text = f"Пользователь {client_telegram_id} хочет пополнить свой депозит на сумму {amount} руб."
    await send_message(admin.telegram_id, text, confirm_update_deposit_markup(client_telegram_id, amount))


async def notify_admin_about_withdrawal(client_telegram_id, amount):
    admin = BotAdminsModel.get_active_bot_admin()
    text = f"Пользователь {client_telegram_id} хочет вывести со своего счета сумму {amount} руб."
    await send_message(admin.telegram_id, text, confirm_withdrawal_markup(client_telegram_id, amount))


