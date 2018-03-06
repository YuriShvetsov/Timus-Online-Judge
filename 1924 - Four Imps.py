#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1924. Four Imps'''

n = int(input())

a = list(range(1, n + 1))

result_1 = a[0]
for i in a[1:]:
    if i % 2 != 0:
        result_1 += i
    else:
        result_1 -= i

result_2 = a[0]
for i in a[1:]:
    if i % 2 != 0:
        result_2 -= i
    else:
        result_2 += i

if result_1 % 2 != 0 and result_2 % 2 != 0:
    print('grimy')
else:
    print('black')
