#!/usr/bin/python
import dateutil.parser

# 解析支持各种格式的
print(dateutil.parser.DEFAULTPARSER.parse("2023-08-08"))
print(dateutil.parser.DEFAULTPARSER.parse("2023-08-09 00:00:00"))
print(dateutil.parser.DEFAULTPARSER.parse("2023-08-10 00:00"))

# 日期差，diff是timedelta类型
date1 = dateutil.parser.DEFAULTPARSER.parse("2023-08-08")
date2 = dateutil.parser.DEFAULTPARSER.parse("2023-08-09 00:00:00")
diff = date2 - date1
print(diff)
print(diff.days)


def xxx():
    print("xxxx")
