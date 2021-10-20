from aiogram import types
from loader import dp

from keyboards.inline.clients import confirm_markup, confirm_callback, back_to_confirm_markup, back_to_confirm_callback


@dp.message_handler(text="Пополнить счет")
async def update_deposit(message: types.Message):
    await message.answer(
        text="Информационный блок, об условиях, пополнения, вывода, получения прибыли",
        reply_markup=confirm_markup()
    )


@dp.callback_query_handler(confirm_callback.filter())
async def confirm_callback(callback: types.CallbackQuery, callback_data: dict):
    await callback.answer()
    choice = callback_data.get('choice')

    if choice == "True":
        ...
    else:
        await callback.message.edit_text(
            text="Информационный блок, что счет нельзя пополнить не подписав согласие",
            reply_markup=back_to_confirm_markup()
        )


@dp.callback_query_handler(back_to_confirm_callback.filter())
async def back_to_confirm(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text="Информационный блок, об условиях, пополнения, вывода, получения прибыли",
        reply_markup=confirm_markup()
    )






