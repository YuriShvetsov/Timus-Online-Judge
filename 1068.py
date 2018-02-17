#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1068. Sum'''

x = int(input())
if x > 0:
    print(sum(list(range(1, x + 1))))
elif x <= 0:
    print(sum(list(range(x, 2))))
