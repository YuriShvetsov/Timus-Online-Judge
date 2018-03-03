#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1585. Penguins'''

import sys


n = int(input())
penguins = []
for line in sys.stdin:
    penguins.append(line[:-1])

p1 = 'Emperor Penguin'
p2 = 'Macaroni Penguin'
p3 = 'Little Penguin'

n1 = 0
n2 = 0
n3 = 0

for i in penguins:
    if i == p1:
        n1 += 1
    elif i == p2:
        n2 += 1
    else:
        n3 += 1

if n1 > n2 and n1 > n3:
    print(p1)
elif n2 > n1 and n2 > n3:
    print(p2)
else:
    print(p3)
