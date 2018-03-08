#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1079. Maximum'''

import sys
import time

numbers = []
for line in sys.stdin:
    numbers.append(int(line[:-1]))

mem = [0, 1]
max_ = [0, 1]


def find_max(num):
    k = 2
    while k < num + 1:
        if k % 2 != 0:
            mem.insert(k, (mem[int(k/2)] + mem[int(k/2+1)]))
        else:
            mem.insert(k, mem[int(k/2)])

        if mem[k] > max_[k-1]:
            max_.insert(k, mem[k])
        else:
            max_.insert(k, max_[k-1])

        k += 1

    return max_[num]


find_max(99999)

what = max_[0]
numbers_2 = []
values = []
h = 0
while h < len(max_):
    if what < max_[h]:
        what = max_[h]

        numbers_2.append(h)
        values.append(what)
    h += 1


for i in numbers[:-1]:
    k = 0
    m = 1
    while m != 0:
        if numbers_2[k] == i:
            print(values[k])
            m = 0
        elif numbers_2[k] > i:
            print(values[k - 1])
            m = 0
        else:
            k += 1
            if k > len(numbers_2) - 1:
                print(values[len(numbers_2) - 1])
                m = 0
