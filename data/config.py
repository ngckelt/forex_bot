from dataclasses import dataclass
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")


DEFAULT_USERNAME = "Отсутствует"


@dataclass
class BotTexts:
    bot_owner = "Информация о владельце бота и услугах которые предоставляет"
    terms_of_deposit_update = "Информационный блок об условиях пополнения, вывода, получения прибыли"
    do_not_confirm_terms = "Информационный блок, что счет нельзя пополнить не подписав согласие"
    commission_percentages = "Информационный блок с % комиссии"


