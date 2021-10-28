from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

confirm_payout_callback = CallbackData('confirm_payout', 'data')


def confirm_payout_markup():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="Подтвердить",
            callback_data=confirm_payout_callback.new("True")
        )
    )
    return markup

