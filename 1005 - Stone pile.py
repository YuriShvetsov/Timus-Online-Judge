#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1005. Stone pile'''

def rec(pile1, pile2, k): # Search of stone piles close in weight
    global _min
    if k == number:
        if (_min > abs(pile1 - pile2)):
            _min = abs(pile1 - pile2)

    else:
        rec(pile1 + a[k], pile2, k + 1)
        rec(pile1, pile2 + a[k], k + 1)

number = int(input()) # Number of stones

a = []
for i in input().split(' '):
    a.append(int(i))

_min = 99999999 # Minimum difference between piles

rec(0, 0, 0)
print(_min)
