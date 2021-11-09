from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp
from datetime import datetime, timezone
from keyboards.default.clients import main_markup
from utils.db_api.db import ClientsModel, BotTextsModel
from states.clients import RegisterClient
from .utils import correct_full_name, correct_card_number, split_card_number
from data.config import BotTexts


@dp.message_handler(CommandStart())
async def start(message: types.Message, state: FSMContext):
    client = await ClientsModel.get_client_by_telegram_id(message.from_user.id)
    if client is None:
        referer_telegram_id = message.get_args()
        referrer = None
        if referer_telegram_id:
            try:
                referer_telegram_id = int(referer_telegram_id)
                if referer_telegram_id == message.from_user.id:
                    await message.answer("Вы не можете быть рефералом для самого себя")
                    return
                referrer = await ClientsModel.get_client_by_telegram_id(referer_telegram_id)
            except ValueError:
                await message.answer("Неверная ссылка")
                return
        await state.update_data(referrer=referrer)
        await message.answer(
            text=await BotTextsModel.get_bot_text_by_item(BotTexts.bot_owner),
        )

        await message.answer("Напишите свою фамилию, свое имя и свое отчество через пробел")
        await RegisterClient.get_full_name.set()
    else:
        await message.answer("Вы уже использовали данную команду", reply_markup=main_markup)


@dp.message_handler(state=RegisterClient.get_full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    if correct_full_name(full_name):
        last_name, first_name, middle_name = full_name.split(' ')
        await state.update_data(
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name
        )

        await message.answer("Пришлите номер Вашей карты. При выводе денег Вы сможете указать "
                             "другую. При отправке номера карты для удобства можно использовать пробелы")
        await RegisterClient.get_card_number.set()
    else:
        await message.answer("Фамилия, имя и отчество указаны в неверном формате")


@dp.message_handler(state=RegisterClient.get_card_number)
async def get_card_number(message: types.Message, state: FSMContext):
    card_number = message.text
    if correct_card_number(card_number):
        state_data = await state.get_data()
        referrer = state_data.get('referrer')
        card_number = split_card_number(card_number)
        try:
            await ClientsModel.add_client(
                message.from_user.id,
                username=message.from_user.username,
                referer=referrer,
                first_name=state_data.get('first_name').capitalize(),
                last_name=state_data.get('last_name').capitalize(),
                middle_name=state_data.get('middle_name').capitalize(),
                card_number=card_number,
                last_update_deposit_date=datetime.now(timezone.utc),
            )
        except Exception as e:
            print(e)
            print(e.__dict__)
            await message.answer("При добавлении записи возникла ошибка. Повторите попытку позже")
            return
        await message.answer(
            text="Регистрация завершена",
            reply_markup=main_markup
        )
        await state.finish()

    else:
        await message.answer("Неверный формат номера карты")





