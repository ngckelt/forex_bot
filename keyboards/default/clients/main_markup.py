from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Пополнить счет"),
            KeyboardButton(text="Депозит")
        ],
        [
            KeyboardButton(text="Вывод средств")
        ]
    ],
    resize_keyboard=True
)
