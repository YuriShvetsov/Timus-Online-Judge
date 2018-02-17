#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1639. Chocolate 2'''

a = [int(x) for x in input().split(' ')]

chocolate_bar = a[0] * a[1]

if chocolate_bar % 2 == 0:
    print('[:=[first]')
else:
    print('[second]=:]')
