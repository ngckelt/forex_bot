from asgiref.sync import sync_to_async
from admin.adminbot.models import *


class ClientsModel:

    @staticmethod
    @sync_to_async
    def add_client(telegram_id, username, referer, **data):
        if username:
            if referer:
                Clients.objects.create(telegram_id=telegram_id, username=username, referer=referer, **data)
            else:
                Clients.objects.create(telegram_id=telegram_id, username=username, **data)
        else:
            if referer:
                Clients.objects.create(telegram_id=telegram_id, referer=referer, **data)
            else:
                Clients.objects.create(telegram_id=telegram_id, **data)

    @staticmethod
    @sync_to_async
    def get_client_by_telegram_id(telegram_id):
        return Clients.objects.filter(telegram_id=telegram_id).first()

    @staticmethod
    @sync_to_async
    def update_client(telegram_id, **update_data):
        Clients.objects.filter(telegram_id=telegram_id).update(**update_data)

    @staticmethod
    @sync_to_async
    def get_clients():
        return Clients.objects.all()

    @staticmethod
    @sync_to_async
    def get_referrals(client):
        return Referrals.objects.filter(referrer=client)


class BotAdminsModel:

    @staticmethod
    @sync_to_async
    def get_bot_admins():
        return BotAdmins.objects.all()

    @staticmethod
    @sync_to_async
    def get_active_bot_admins():
        return BotAdmins.objects.filter(active=True)

    @staticmethod
    @sync_to_async
    def get_active_bot_admin():
        return BotAdmins.objects.filter(active=True).first()


class ReferralsModel:

    @staticmethod
    @sync_to_async
    def add_referral(referrer, referral_telegram_id, referral_username):
        if referral_username:
            Referrals.objects.create(
                referrer=referrer,
                telegram_id=referral_telegram_id,
                username=referral_username
            )
        else:
            Referrals.objects.create(
                referrer=referrer,
                telegram_id=referral_telegram_id,
            )


