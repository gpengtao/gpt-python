#!/usr/bin/python
import time

from apscheduler.schedulers.blocking import BlockingScheduler


def print_num():
    print("hello")
    time.sleep(5)


# BlockingScheduler：适用于调度程序是进程中唯一运行的进程，调用 start函数会阻塞当前线程，不能立即返回。
scheduler = BlockingScheduler()
scheduler.add_job(print_num, 'interval', seconds=1)
scheduler.start()

print("不会走到这里")
time.sleep(10000)
