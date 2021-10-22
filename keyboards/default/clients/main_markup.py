from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Пополнить счет"),
            KeyboardButton(text="Депозит")
        ],
        [
            KeyboardButton(text="Вывод средств"),
            KeyboardButton(text="Реферальная ссылка")
        ]
    ],
    resize_keyboard=True
)
