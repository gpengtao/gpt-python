#!/usr/bin/python
import time

from apscheduler.schedulers.blocking import BlockingScheduler


def print_num():
    print("hello")
    time.sleep(5)


scheduler = BlockingScheduler()
scheduler.add_job(print_num, 'interval', seconds=1)
scheduler.start()

time.sleep(10000)
