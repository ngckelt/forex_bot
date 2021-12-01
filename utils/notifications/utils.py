from loader import bot
from data.config import DEFAULT_USERNAME


async def send_message(chat_id, text, reply_markup):
    await bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=reply_markup
    )


async def send_message_to_client(client_telegram_id, text, reply_markup=None):
    try:
        await send_message(client_telegram_id, text, reply_markup)
    except Exception as e:
        ...
        # await send_message("802019362", e, None)


async def send_message_to_admin(admin, text, reply_markup=None):
    try:
        await send_message(admin.telegram_id, text, reply_markup)
    except Exception as e:
        ...
        # await send_message("802019362", e, None)


async def send_message_to_referrer(referrer_telegram_id, text, reply_markup=None):
    try:
        await send_message(referrer_telegram_id, text, reply_markup)
    except Exception as e:
        ...
        # await send_message("802019362", e, None)


def get_user_contact(user):
    message = f"<b>{user.last_name} {user.first_name} {user.middle_name}</b>"
    if user.username != DEFAULT_USERNAME:
        message += f" @{user.username}"
    return message

