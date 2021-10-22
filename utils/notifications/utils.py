from loader import bot


async def send_message(chat_id, text, reply_markup=None):
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup
        )
    except Exception as e:
        raise ValueError(f"Cannot send data to user {chat_id}")


