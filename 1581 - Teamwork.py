#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1581. Teamwork'''

import sys

n = int(input())
numbers = []
for line in sys.stdin:
    for i in line.split():
        numbers.append(int(i))

k = 1
m = 1
lst = []
for number in numbers:
    if k < len(numbers):
        if number == numbers[k]:
            m += 1
        else:
            lst.append(m)
            lst.append(number)
            m = 1
    else:
        lst.append(m)
        lst.append(number)
    k += 1

print(*lst)
