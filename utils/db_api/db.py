from asgiref.sync import sync_to_async
from admin.adminbot.models import *
from data.config import DEFAULT_USERNAME


class ClientsModel:

    @staticmethod
    @sync_to_async
    def add_client(telegram_id, username, referer, **data):
        if not username:
            username = DEFAULT_USERNAME
        if referer:
            Clients.objects.create(telegram_id=telegram_id, username=username, referer=referer, **data)
        else:
            Clients.objects.create(telegram_id=telegram_id, username=username, **data)

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


class DepositsModel:

    @staticmethod
    @sync_to_async
    def add_deposit(**data):
        Deposits.objects.create(**data)

    @staticmethod
    @sync_to_async
    def get_client_deposits(client_telegram_id):
        return Deposits.objects.filter(telegram_id=client_telegram_id)


class WithdrawalsModel:

    @staticmethod
    @sync_to_async
    def add_withdrawal(**data):
        Withdrawals.objects.create(**data)

    @staticmethod
    @sync_to_async
    def get_client_withdrawals(client_telegram_id):
        return Withdrawals.objects.filter(telegram_id=client_telegram_id)

    @staticmethod
    @sync_to_async
    def get_last_client_withdrawal(client_telegram_id):
        return Withdrawals.objects.filter(telegram_id=client_telegram_id).order_by('-datetime').first()


class ReferralAccrualsModel:

    @staticmethod
    @sync_to_async
    def add_referral_accrual(**data):
        ReferralAccruals.objects.create(**data)


class CardDetailsModel:

    @staticmethod
    @sync_to_async
    def get_card_details():
        return CardDetails.objects.all()


class BotTextsModel:

    @staticmethod
    @sync_to_async
    def get_bot_text_by_item(item):
        texts = BotTexts.objects.all()
        for text in texts:
            if text.name == item:
                return text.text





