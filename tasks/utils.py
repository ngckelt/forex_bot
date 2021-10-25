from handlers.admins.utils import TEN_PERCENT, ONE_PERCENT


def count_bonus(current_deposit):
    return float(current_deposit) * TEN_PERCENT


def count_referrer_bonus(amount):
    return float(amount) * ONE_PERCENT

