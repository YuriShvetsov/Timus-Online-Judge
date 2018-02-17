#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1820. Ural steacks'''

a = []
for i in input().split(' '):
    a.append(int(i))
n = a[0]; k = a[1]

if k > n:
    n = k

n = 2 * n

if n % k == 0:
    print(int(n / k))
else:
    print(int(n / k + 1))
