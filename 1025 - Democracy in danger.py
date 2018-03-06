#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1025. Democracy in danger'''

# Input of data
num = int(input())
voters = [int(x) for x in input().split(' ')]


# Calculation of the required number of groups
if num % 2 != 0:
    required_groups = num - num // 2
else:
    required_groups = num - num // 2 + 1

# Calculation of the required number of voters
voters = sorted(voters)
k = 0
required_voters = 0
while k < required_groups:
    if voters[k] % 2 != 0:
        required_voters += voters[k] - voters[k] // 2
    else:
        required_voters += voters[k] - voters[k] // 2 + 1
    k += 1


print(required_voters)
