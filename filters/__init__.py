from aiogram import Dispatcher

from .admin_filters import AdminOnly


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminOnly)
