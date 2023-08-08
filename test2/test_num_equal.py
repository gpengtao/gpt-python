#!/usr/bin/python

def get_num():
    return 3


def get_string_num():
    return "3"


num = get_num()
string_num = get_string_num()

print(num == string_num)
print(num == int(string_num))
