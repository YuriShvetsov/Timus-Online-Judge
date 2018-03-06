#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1209. 1, 10, 100, 1000...'''

import sys
import math

# Search for the sum of a sequence of natural numbers
def theSumNum(num):
    return int(num*(num + 1) / 2)

# Search for a sequence value
def searchNum(sumN):
    return int((-1 + math.sqrt(1 + (8 * sumN))) // 2)

# Input
n = int(input())
numbers = []
for line in sys.stdin:
    for i in line.split():
        numbers.append(int(i))

# Main
items = ''
for i in numbers:
    if i == 1:
        items += '1 '
    else:
        if theSumNum(searchNum(i)) == i - 1:
            items += '1 '
        else:
            items += '0 '

print(items)
