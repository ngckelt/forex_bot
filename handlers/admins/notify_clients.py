from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp, bot

from utils.db_api.db import ClientsModel
from keyboards.inline import yes_or_no_markup, yes_or_no_callback
from filters.admin_filters import AdminOnly
from states.admins import NotifyClients


from tasks.monthly_accruals import accrual_months_percents


# @dp.message_handler(commands=['test'])
# async def test(message: types.Message):
#     await accrual_months_percents()


@dp.message_handler(AdminOnly(), commands=['mailing'])
async def start_notify(message: types.Message):
    await message.answer("Пришлите текст рассылки")
    await NotifyClients.get_text.set()


@dp.message_handler(AdminOnly(), state=NotifyClients.get_text)
async def get_text(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text, images=[])
    await message.answer(
        text="Нужно добавить фото?",
        reply_markup=yes_or_no_markup("add_photo")
    )
    await NotifyClients.ask_photo.set()


@dp.callback_query_handler(AdminOnly(), yes_or_no_callback.filter(question="add_photo"),
                           state=NotifyClients.ask_photo)
async def ask_photo(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.answer()
    choice = callback_data.get("choice")
    if choice == 'yes':
        await callback.message.answer("Пришлите фото")
        await NotifyClients.get_photo.set()
    else:
        state_data = await state.get_data()
        images = state_data.get('images')
        text = state_data.get('text')
        album = types.MediaGroup()
        for image in images:
            album.attach_photo(image)

        if album.to_python():
            await callback.message.answer_media_group(media=album)
        await callback.message.answer(text)

        await callback.message.answer(
            text="Это будет выглядеть так. Отправить?",
            reply_markup=yes_or_no_markup("send")
        )

        await NotifyClients.confirm.set()


@dp.message_handler(AdminOnly(), state=NotifyClients.get_photo, content_types=types.ContentTypes.PHOTO)
async def get_photo(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    images = state_data.get("images")
    img_id = message.photo[-1].file_id
    images.append(img_id)
    await state.update_data(images=images)
    await message.answer(
        text="Добавить еще фото?",
        reply_markup=yes_or_no_markup("add_photo")
    )
    await NotifyClients.ask_photo.set()


@dp.callback_query_handler(AdminOnly(), yes_or_no_callback.filter(question="send"),
                           state=NotifyClients.confirm)
async def send_data(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.answer()
    choice = callback_data.get("choice")
    if choice == 'yes':
        await callback.message.answer("Рассылка запущена")
        state_data = await state.get_data()
        images = state_data.get('images')
        text = state_data.get('text')
        album = types.MediaGroup()
        for image in images:
            album.attach_photo(image)

        clients = await ClientsModel.get_clients()

        for client in clients:
            try:
                if album.to_python():
                    await bot.send_media_group(
                        chat_id=client.telegram_id,
                        media=album
                    )

                await bot.send_message(
                    chat_id=client.telegram_id,
                    text=text,
                )
            except Exception as e:
                await callback.message.answer(
                    text=f"Не удалось отправить сообщение клиенту с id {client.telegram_id}. "
                         f"Возможно, он удалил чат с ботом"
                )

        await callback.message.answer("Рассылка успешно завершена")

    else:
        await callback.message.answer("Чтобы заново сформировать данные для рассылки, воспользуйтесь "
                                      "соответствующей кнопкой")
    await state.finish()
