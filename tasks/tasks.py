import aioschedule
from asyncio import sleep
from .monthly_accruals import accrual_ten_percent

BASE_SLEEP_SECONDS = 1


async def setup():
    # aioschedule.every().minute.do(accrual_ten_percent)
    # aioschedule.every().day.at("21:45").do(accrual_ten_percent)

    while True:
        await aioschedule.run_pending()
        await sleep(BASE_SLEEP_SECONDS)

