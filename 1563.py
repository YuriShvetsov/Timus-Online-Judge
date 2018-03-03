#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1563. Bayan'''

import sys


n = int(input())
shops = []
for line in sys.stdin:
    shops.append(line[:-1])

shops = sorted(shops)

s = shops[0]
k = 0
for i in shops[1:]:
    if i == s:
        k += 1
    s = i

print(k)
