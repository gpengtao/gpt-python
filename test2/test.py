#!/usr/bin/python
import json

myList = ['a', 'b', 'c', 'd']

for one in myList:
    if one == 'b':
        myList.remove(one)

print(myList)

xx1 = ['c', 'd']
xx2 = ['d', 'e']

yy = list(filter(lambda one: one in xx1 and one in xx2, myList))

print(yy)

print(json.dumps(myList))