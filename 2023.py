#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''2023. Donald is a postman'''

import sys

number = int(input())
zero = []
for line in sys.stdin:
    zero.append(line[:-1])

first = ['Alice', 'Ariel', 'Aurora', 'Phil', 'Peter', 'Olaf', 'Phoebus', 'Ralph', 'Robin']
second = ['Bambi', 'Belle', 'Bolt', 'Mulan', 'Mowgli', 'Mickey', 'Silver', 'Simba', 'Stitch']
third = ['Dumbo', 'Genie', 'Jiminy', 'Kuzko', 'Kida', 'Kenai', 'Tarzan', 'Tiana', 'Winnie']

items = []

for i in zero:
    for j in first:
        if i == j:
            items.append(1)
    for j in second:
        if i == j:
            items.append(2)
    for j in third:
        if i == j:
            items.append(3)
if items[0] != 1:
    items.insert(0, 1)
else:
    pass

k = 0
while k < len(items) - 1:
    if abs(items[k] - items[k + 1]) > 1:
        if items[k] > items[k + 1]:
            items.insert(k + 1, items[k] - 1)
        else:
            items.insert(k + 1, items[k] + 1)
    elif items[k] == items[k + 1]:
        items.pop(k)
    else:
        k += 1

print(len(items) - 1)
