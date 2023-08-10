#!/usr/bin/python
import time

from apscheduler.schedulers.background import BackgroundScheduler


def print_num():
    print("hello")


# BackgroundScheduler：适用于调度程序在应用程序的后台运行，调用 start后主线程不会阻塞。
scheduler = BackgroundScheduler()
scheduler.add_job(print_num, 'interval', seconds=5)
scheduler.start()

print("会走到这里")
time.sleep(10000)
