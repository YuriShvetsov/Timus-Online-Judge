#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1005. Stone pile'''

import math

def rec(k1, k2, x):
    global _min
    if x == count:
        if (_min > abs(k1 - k2)):
            _min = abs(k1 - k2)

    else:
        rec(k1 + a[x], k2, x + 1)
        rec(k1, k2 + a[x], x + 1)

count = int(input())

a = []
for i in input().split(' '):
    a.append(int(i))

_min = 99999999

rec(0, 0, 0)
print(_min)
