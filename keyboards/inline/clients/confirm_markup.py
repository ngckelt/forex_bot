from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

confirm_callback = CallbackData('confirm', 'choice')
back_to_confirm_callback = CallbackData('back_to_confirm', 'data')


def confirm_markup():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="Подтверждаю",
            callback_data=confirm_callback.new("True")
        )
    )
    markup.add(
        InlineKeyboardButton(
            text="Отказываюсь",
            callback_data=confirm_callback.new("False")
        )
    )
    return markup


def back_to_confirm_markup():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="Назад",
            callback_data=back_to_confirm_callback.new("True")
        )
    )
    return markup


