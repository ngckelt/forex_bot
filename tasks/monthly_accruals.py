from pprint import pprint

from utils.db_api.db import ClientsModel, ReferralAccrualsModel, DepositsModel, WithdrawalsModel
from handlers.admins.utils import get_delta_days, get_current_month_number, get_month_days_quantity
from datetime import datetime, timezone, timedelta
# from utils.notifications import notify_client_about_ten_percent_deposit_update, \
#     notify_admin_about_ten_percent_deposit_update, notify_referrer_about_one_percent_deposit_update, \
#     notify_admin_about_one_percent_deposit_update
from .utils import count_bonus, count_referrer_bonus

MONTH_DEPOSIT_UPDATE_DELTA_DAYS = 30


async def has_withdrawals(client):
    previous_month_number = get_current_month_number() - 1
    client_withdrawals = await WithdrawalsModel.get_client_withdrawals(client.telegram_id)
    for client_withdrawal in client_withdrawals:
        if int(client_withdrawal.datetime.strftime('%m')) == previous_month_number:
            return True
    return False


async def get_previous_month_deposit_updates(client):
    updates = list()
    previous_month_number = get_current_month_number() - 1
    deposit_updates = await DepositsModel.get_client_deposits(client.telegram_id)
    for deposit_update in deposit_updates:
        if int(deposit_update.datetime.strftime('%m')) == previous_month_number:
            updates.append(deposit_update)
    return updates


"""
Решили что вычисляем количетсво дней до 1 числа, делим на число дней в месяце, 
вычисляем % начисления. 
Далее все начисления происходят с 1 по 1 число вне зависимости от количества дней в месяце.
"""
async def accrual_months_percents():
    now = datetime.now(timezone.utc)
    previous_month_number = get_current_month_number() - 1
    previous_month_days_quantity = get_month_days_quantity(previous_month_number)
    clients = await ClientsModel.get_clients()
    for client in clients:
        if not await has_withdrawals(client):
            print("Выводов в предыдущем месяце нет")
            previous_month_deposit_updates = await get_previous_month_deposit_updates(client)

            for deposit_update in previous_month_deposit_updates:
                # pprint(deposit_update.__dict__)
                delta_days = previous_month_days_quantity - int(deposit_update.datetime.strftime('%d'))
                percent = delta_days / previous_month_days_quantity / 100
                print(previous_month_days_quantity, int(deposit_update.datetime.strftime('%d')), delta_days, percent, deposit_update.amount)
                bonus = float(deposit_update.amount) * percent

                print(bonus)
                print("*" * 30)

        else:
            print("Выводы в предыдущем месяце есть")

"""
Вопрос по поводу вычисления суммы месячного начисления

Допустим ситуация такая:

Пользователь вснес 5000 19 сентября и 10 000 25 сентября

Для 5000 разница в днях составит 30 - 19 = 11, и соответственно процент 11 / 30 = 0.37
далее 5000 * 0.37 = 1833.38, это получился первый бонус

Для 10 000 разница в днях равна 5 и процент 5/30 = 0.17
потом 10 000 * 0.17 = 1666.67, это второй бонус 

И соответственно потом эти два бонуса сложить и получится итоговая сумма начисления

Это правильно посчитано, или нет?

"""

# async def accrual_ten_percent():
#     now = datetime.now(timezone.utc)
#     clients = await ClientsModel.get_clients()
#     for client in clients:
#         dd = get_delta_days(now, client.last_update_deposit_date)
#         print(dd)
#         if get_delta_days(now, client.last_update_deposit_date) == MONTH_DEPOSIT_UPDATE_DELTA_DAYS:
#             bonus = count_bonus(client.deposit)
#             await ClientsModel.update_client(client.telegram_id, deposit=client.deposit + bonus)
#             await notify_client_about_ten_percent_deposit_update(client.telegram_id, bonus, client.deposit + bonus)
#             await notify_admin_about_ten_percent_deposit_update(client.telegram_id, bonus)
#
#             if client.referer:
#                 referrer = await ClientsModel.get_client_by_telegram_id(client.referer)
#                 referrer_bonus = count_referrer_bonus(bonus)
#                 await ClientsModel.update_client(referrer.telegram_id, deposit=referrer.deposit + referrer_bonus)
#                 await notify_referrer_about_one_percent_deposit_update(referrer.telegram_id, client.telegram_id,
#                                                                        referrer_bonus)
#                 await notify_admin_about_one_percent_deposit_update(referrer.telegram_id, client.telegram_id, bonus,
#                                                                     referrer_bonus)
#                 await ReferralAccrualsModel.add_referral_accrual(
#                     amount=referrer_bonus,
#                     accrual_to=referrer.telegram_id,
#                     accrual_from=client.telegram_id,
#                     datetime=now,
#                 )
#




