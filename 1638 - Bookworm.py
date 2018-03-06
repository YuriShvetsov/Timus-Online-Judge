#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1638. Bookworm'''

data = [int(x) for x in input().split(' ')]

if data[3] > data[2]:
    k = abs(data[3] - data[2])
    k2 = k - 1
    print(k2 * data[0] + data[1] * k * 2)
else:
    k = abs(data[3] - data[2]) + 1
    k2 = k - 1
    print(k * data[0] + data[1] * k2 * 2)
