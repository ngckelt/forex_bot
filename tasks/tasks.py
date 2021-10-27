import aioschedule
from asyncio import sleep
from .monthly_accruals import accrual_months_percents

BASE_SLEEP_SECONDS = 1


async def setup():
    ...
    # aioschedule.every().minute.do(accrual_months_percents)
    # aioschedule.every().day.at("21:45").do(accrual_ten_percent)

    # while True:
    #     await aioschedule.run_pending()
    #     await sleep(BASE_SLEEP_SECONDS)

"""
Решили что вычисляем количетсво дней до 1 числа, делим на число дней в месяце, вычисляем % начисления. 
Далее все начисления происходят с 1 по 1 число вне зависимости от количества дней в месяце.
"""



