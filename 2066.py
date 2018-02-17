#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''2066. Simple Expression'''

import sys

nums = []
for line in sys.stdin:
    for i in line.split():
        nums.append(int(i))

nums = sorted(nums)

a = nums[0]
b = nums[1]
c = nums[2]
result = 0

if a == 0:
    if a == b or b == 1:
        result = a - b - c
    else:
        result = a - b * c
elif a == 1:
    if a == b:
        result = a - b - c
    else:
        result = a - b * c
else:
    result = a - b * c

print(result)
