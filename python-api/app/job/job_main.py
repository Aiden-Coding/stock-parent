# -------------------------------------------------
import time

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.service.stock import insert_of_null_stock,update_cn_ths_stock_block


def cron_job():
    print('打印当前时间:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


async def update_stock_base_infoT():
    # generate a URL for the endpoint `post_handler`
    scheduler = AsyncIOScheduler()
    # scheduler.add_job(cron_job, CronTrigger.from_crontab('*/1 * * * *'))
    scheduler.add_job(update_stock_base_infohel, CronTrigger.from_crontab('26 9 * * *'))
    scheduler.add_job(update_cn_ths_stock_block_db, CronTrigger.from_crontab('26 9 * * *'))
    scheduler.start()


# 定时任务函数 ，此处可以是async。也可以不是异步函数
# 更新A股基本数据
def update_stock_base_infohel():
    insert_of_null_stock()


# 定时任务函数 ，此处可以是async。也可以不是异步函数
# 更新A股基本数据
def update_cn_ths_stock_block_db():
    update_cn_ths_stock_block()
