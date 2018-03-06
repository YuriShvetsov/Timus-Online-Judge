#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1293. Eniya'''

a = []
for i in input().split(' '):
    a.append(int(i))
    
def multiply(lst):
    answer = 1
    for i in lst:
        answer *= i
    return answer
    
print(multiply(a) * 2)
