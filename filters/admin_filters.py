from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from utils.db_api.db import BotAdminsModel


class AdminOnly(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        bot_admins = await BotAdminsModel.get_active_bot_admins()
        bot_admins_id = [admin.telegram_id for admin in bot_admins]
        return str(message.from_user.id) in bot_admins_id

