from datetime import datetime, timezone

TEN_PERCENT = 10 / 100
TWO_PERCENT = 2 / 100


def get_current_month_number():
    return int(datetime.now().strftime("%m"))


def get_delta_days(current_date, past_date):
    return (current_date - past_date).days


def get_month_days_quantity(month_number):
    return (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[month_number-1]


def count_deposit(current_deposit, amount, last_deposit_update_date):
    now = datetime.now(timezone.utc)
    delta_days = get_delta_days(now, last_deposit_update_date)
    days_quantity = get_month_days_quantity(get_current_month_number())
    bonus = round(current_deposit * TEN_PERCENT * delta_days / days_quantity, 2)
    return current_deposit + amount + bonus


def count_referrer_two_percent_deposit_update(amount):
    return amount * TWO_PERCENT


if __name__ == '__main__':
    ...
    # last_update_deposit_date = datetime(2021, 10, 1)
    # now = datetime.now()
    # current_deposit = 10000
    # months_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # current_month_number = int(now.strftime("%m"))
    #
    # delta_days = (now - last_update_deposit_date).days
    # # rint(delta_days, type(delta_days))
    #
    # new_deposit = 5000
    #
    # d = round(current_deposit * 1/10 * delta_days / months_days[current_month_number - 1], 2)
    # d += current_deposit + new_deposit
    # print(d)

    # print(months_days[current_month_number-1])
"""
Повторное пополнение депозита:
текущий депозит * на 10% * на количество дней которых прошло со дня 
начисления процента / на количество дней месяца + текущий депозит
К этой сумме прибавляется новая сумма пополнения. И дата начисления 
процентов изменяется на дату зачисления последнего депозита. 
Пример: то есть к примеру пополнил первого октября 10000
дальше еще пополнил 7 октября пополнил на 10000 получится:
10000*7 / 31*10% = 225.80руб + 10000(начальный депозит) + 
10000 (новый депозит) итого 20225.80. 
И следующее начисление 10% будет происходить 7 ноября
"""


