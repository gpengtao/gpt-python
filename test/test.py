#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author pengtao.geng Created on 2019-07-01 19:12
"""


def fib_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


print fib_recur(35)
