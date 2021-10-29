from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp

from keyboards.inline.clients import confirm_markup, confirm_callback, back_to_confirm_markup, back_to_confirm_callback
from keyboards.inline import yes_or_no_markup, yes_or_no_callback
from keyboards.inline.clients import confirm_payout_markup, confirm_payout_callback
from keyboards.default.clients import cancel_markup, main_markup
from states.clients import UpdateDeposit
from .utils import correct_update_amount, correct_card_number, split_card_number, count_commission
from utils.notifications import notify_admin_about_update_deposit
from utils.db_api.db import ClientsModel, BotTextsModel, CardDetailsModel
from data.config import BotTexts


@dp.message_handler(text="Пополнить счет")
async def update_deposit(message: types.Message):
    await message.answer(
        text=await BotTextsModel.get_bot_text_by_item(BotTexts.terms_of_deposit_update),
        reply_markup=confirm_markup()
    )


@dp.callback_query_handler(confirm_callback.filter())
async def confirm_callback(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.answer()
    choice = callback_data.get('choice')

    if choice == "True":
        card_details = await CardDetailsModel.get_card_details()
        text = ""
        for card_detail in card_details:
            text += f"{card_detail.card_name}: {card_detail.card_number}\n"
        await callback.message.answer(text, reply_markup=confirm_payout_markup())
    else:
        await callback.message.edit_text(
            text=await BotTextsModel.get_bot_text_by_item(BotTexts.do_not_confirm_terms),
            reply_markup=back_to_confirm_markup()
        )


@dp.callback_query_handler(confirm_payout_callback.filter())
async def confirm_payout(callback: types.CallbackQuery, callback_data: dict):
    await callback.answer()
    await callback.message.answer("Пришлите сумму, котрую вы перевели")
    await UpdateDeposit.get_amount.set()


@dp.callback_query_handler(back_to_confirm_callback.filter())
async def back_to_confirm(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=await BotTextsModel.get_bot_text_by_item(BotTexts.terms_of_deposit_update),
        reply_markup=confirm_markup()
    )


@dp.message_handler(state=UpdateDeposit.get_amount)
async def get_amount(message: types.Message, state: FSMContext):
    amount = message.text.replace(' ', '')
    if correct_update_amount(amount):
        state_data = await state.get_data()
        card_number = state_data.get('card_number')
        try:
            client = await ClientsModel.get_client_by_telegram_id(message.from_user.id)
            deposit, commission = count_commission(amount)
            await notify_admin_about_update_deposit(client, amount, deposit, commission)
            await message.answer(f"Депозит будет пополнен на {deposit} руб\n"
                                 f"Комиссия за пополнение составила {commission} руб")
            await message.answer("Заявка отправлена администратору. Ожидайте ответ", reply_markup=main_markup)
        except ValueError:
            await message.answer("При отправке данных администратору возникла непредвиденная ошибка. "
                                 "Повторите попытку позже", reply_markup=main_markup)
        await state.finish()
    else:
        await message.answer("Сумма указана неверно")


# При пополнении:
# Когда чел отправляет 10тр
# Ему приходит сообщение:
# Депозит будет пополнен на 9000руб
# Комиссия за пополнение составила 1000руб



