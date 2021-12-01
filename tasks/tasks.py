import aioschedule
from asyncio import sleep
from .monthly_accruals import accrual_months_percents

BASE_SLEEP_SECONDS = 1


async def setup():
    # aioschedule.every().minute.do(accrual_months_percents)
    # aioschedule.every().day.at("00:00").do(accrual_months_percents)
    aioschedule.every().day.at("13:34").do(accrual_months_percents)

    while True:
        await aioschedule.run_pending()
        await sleep(BASE_SLEEP_SECONDS)




