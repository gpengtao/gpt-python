#!/usr/bin/python

import sys

values = sys.path
for value in values:
    print(value)

sys.path.append('./app')
