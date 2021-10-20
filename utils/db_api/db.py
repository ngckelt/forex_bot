from admin.adminbot.models import *


class ClientsModel:

    @staticmethod
    def add_client(telegram_id, **data):
        Clients.objects.create(telegram_id=telegram_id, **data)

    @staticmethod
    def get_client_by_telegram_id(telegram_id):
        return Clients.objects.filter(telegram_id=telegram_id).first()

    @staticmethod
    def update_client(telegram_id, **update_data):
        Clients.objects.filter(telegram_id=telegram_id).update(**update_data)




