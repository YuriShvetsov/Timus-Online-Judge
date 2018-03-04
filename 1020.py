#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1020. Rope'''

import math
import sys


def main(alist, r, n):
    sides = []
    if n == 1:
        return round((2 * math.pi * r), 2)
    elif n == 2:
        x1 = alist[0]
        y1 = alist[1]
        x2 = alist[2]
        y2 = alist[3]
        if x1 == x2:
            l = abs(y1 - y2)
            sides.append(float(l))
        elif y1 == y2:
            l = abs(x1 - x2)
            sides.append(float(l))
        else:
            delta = abs(x1 - x2)
            delta2 = abs(y1 - y2)
            l = math.sqrt(pow(delta, 2) + pow(delta2, 2))
            sides.append(float(l))

        return round((sum(sides) * 2 + 2 * math.pi * r), 2)
    else:
        x1 = alist[len(alist) - 2]
        y1 = alist[len(alist) - 1]
        k = 0
        while k < len(alist):
            x2 = alist[k]
            y2 = alist[k + 1]
            if y1 == y2:
                l = abs(x1 - x2)
                sides.append(float(l))
                k += 2
            elif x1 == x2:
                l = abs(y1 - y2)
                sides.append(float(l))
                k += 2
            else:
                delta = abs(x1 - x2)
                delta2 = abs(y1 - y2)
                l = math.sqrt(pow(delta, 2) + pow(delta2, 2))
                sides.append(float(l))
                k += 2
            x1 = x2
            y1 = y2

        return round((sum(sides) + 2 * math.pi * r), 2)


data = [float(x) for x in input().split(' ')]
num = int(data[0])
radius = data[1]

coordinates = []
for line in sys.stdin:
    for i in line[:-1].split(' '):
        coordinates.append(float(i))

print(main(coordinates, radius, num))
