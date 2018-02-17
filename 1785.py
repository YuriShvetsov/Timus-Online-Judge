#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1785. Lost in localization'''

m = int(input())
q = ['few', 'several', 'pack', 'lots', 'horde', 'throng', 'swarm', 'zounds', 'legion']

if m >= 1 and m <= 4:
    print(q[0])
elif m >= 5 and m <= 9:
    print(q[1])
elif m >= 10 and m <= 19:
    print(q[2])
elif m >= 20 and m <= 49:
    print(q[3])
elif m >= 50 and m <= 99:
    print(q[4])
elif m >= 100 and m <= 249:
    print(q[5])
elif m >= 250 and m <= 499:
    print(q[6])
elif m >= 500 and m <= 999:
    print(q[7])
elif m >= 1000:
    print(q[8])
