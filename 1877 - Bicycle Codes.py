#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1877. Bicycle codes'''

a = int(input())
b = int(input())

if a % 2 == 0 or b % 2 != 0:
    print('yes')
elif a % 2 != 0 or b % 2 == 0:
    print('no')
else:
    print('no')
