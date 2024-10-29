#!/usr/bin/python

my_dict = {}
print(my_dict)

my_dict["aaa"] = "hello"
print(my_dict)

my_dict['bbb'] = "world"
print(my_dict)

print(my_dict["aaa"])
# get不报错
print(my_dict.get("ccc"))
# []如果key不存在，会报KeyError错误
print(my_dict["ccc"])
