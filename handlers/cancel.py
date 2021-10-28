from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
from keyboards.default.clients import main_markup


@dp.message_handler(text="Отмена", state="*")
async def cancel_action(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text="Действие отменено",
        reply_markup=main_markup
    )

