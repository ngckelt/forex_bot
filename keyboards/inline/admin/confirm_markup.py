from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

confirm_update_deposit_callback = CallbackData('confirm_update_deposit', 'choice', 'amount', 'client_telegram_id')
confirm_withdrawal_callback = CallbackData('confirm_withdrawal', 'choice', 'amount', 'client_telegram_id')


def confirm_update_deposit_markup(client_telegram_id, amount):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="Подтвердить",
            callback_data=confirm_update_deposit_callback.new("confirm", amount, client_telegram_id)
        )
    )
    markup.add(
        InlineKeyboardButton(
            text="Отказать",
            callback_data=confirm_update_deposit_callback.new("not_confirm", amount, client_telegram_id)
        )
    )
    return markup


def confirm_withdrawal_markup(client_telegram_id, amount):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="Подтвердить",
            callback_data=confirm_withdrawal_callback.new("confirm", amount, client_telegram_id)
        )
    )
    markup.add(
        InlineKeyboardButton(
            text="Отказать",
            callback_data=confirm_withdrawal_callback.new("not_confirm", amount, client_telegram_id)
        )
    )
    return markup



