#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1787. Turn on MEGA'''

kn = []
for i in input().split(' '):
    kn.append(int(i))
k = kn[0]; n = kn[1]

cars = []
for i in input().split(' '):
    cars.append(int(i))

traffic = 0
for i in cars:
    traffic += i
    traffic -= k
    if traffic <= 0:
        traffic = 0

print(traffic)
