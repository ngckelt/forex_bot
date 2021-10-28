from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Отмена"),
        ],
    ],
    resize_keyboard=True
)
