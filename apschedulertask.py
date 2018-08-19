# -*- coding:utf-8 -*-

from selenium_chrome import job_geturl1
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time


def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


if __name__ == '__main__':
    # 创建后台执行的 schedulers
    scheduler = BlockingScheduler()
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
    # scheduler.add_job(my_job, 'interval', seconds=5)

    # 放在了单独线程里，所以调用start后主线程不会阻塞
    # scheduler = BackgroundScheduler()

    # 表示2017年3月22日17时19分07秒执行该程序
    scheduler.add_job(job_geturl1, 'cron', year=2018, month=8, day=17, hour=11, minute=37, second=10)
    # 表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
    # scheduler.add_job(job_geturl1, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
    # 表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
    # scheduler.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2014-05-30')
    # 启动调度任务
    print("定时任务启动中...")
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    scheduler.start()

    # while True:
    #     time.sleep(300)




