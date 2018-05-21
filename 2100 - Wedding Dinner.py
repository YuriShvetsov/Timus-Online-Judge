#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''2100. Wedding Dinner'''

import sys

quantity = int(input())
guests = []
for line in sys.stdin:
    guests.append(line[:-1])

for person in guests:
    if person[-4:] == '+one':
        quantity += 1

if quantity == 11:
    print(1400)
else:
    (print(quantity * 100 + 200))
