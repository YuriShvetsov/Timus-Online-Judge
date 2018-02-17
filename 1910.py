#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1910. Titan Ruins: Hidden Entrance'''

n = int(input())
a = [int(x) for x in input().split(' ')]

k = 0
j = 0
b = []
while k < (len(a) - 2):
    j += a[k] + a[k + 1] + a[k + 2]
    b.append(j)
    k += 1
    j = 0

b = sorted(b)

k = 0
h = 0
while k < (len(a) - 2):
    h += a[k] + a[k + 1] + a[k + 2]
    if h == (b[len(b) - 1]):
        print( (b[len(b) - 1]), k + 2 )
        break
    k += 1
    h = 0
