#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1083. Factorials!!!'''

f = input().split()
rst = 1

exc_q = len(f[1])
num = int(f[0])
f2 = [num]

while num > 1:
    num -= exc_q
    if num >= 1:
        f2.append(num)

for i in f2:
    rst *= i

print(rst)
