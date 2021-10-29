from datetime import datetime, timezone

TEN_PERCENT = 10 / 100
# TWO_PERCENT = 2 / 100
ONE_PERCENT = 1 / 100


def get_current_month_day():
    return int(datetime.now(timezone.utc).strftime('%d'))


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
    return round(current_deposit + amount + bonus, 2)


def count_referrer_one_percent_deposit_update(amount):
    return amount * ONE_PERCENT




