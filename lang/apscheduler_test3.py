#!/usr/bin/python
import time

from apscheduler.schedulers.background import BackgroundScheduler

num = 1


def _get_new_value():
    return 100


def set_num_new_value():
    global num
    num = _get_new_value()
    print("set num %s" % num)


scheduler = BackgroundScheduler()
scheduler.add_job(set_num_new_value, 'interval', seconds=1)
scheduler.start()

for i in range(1000000):
    time.sleep(0.1)
    if not num:
        print(num)
