#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1264. Workdays'''

a = []

for i in input().split(' '):
    a.append(int(i))

print(a[0] * (a[1] + 1))
