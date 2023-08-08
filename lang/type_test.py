#!/usr/bin/python
import dateutil.parser

"""
a的类型可以随意更换
"""

a = 10
print(a)

a = "hello world"
print(a)

a = dateutil.parser.DEFAULTPARSER.parse("2023-08-08")
print(a)
