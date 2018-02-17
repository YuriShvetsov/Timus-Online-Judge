#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1880. Psych Up's Eigenvalues'''

def binSearch(li, x):
    k = 0
    if len(li) == 0:
        return k
    else:
        midpoint = len(li) // 2
        if li[midpoint] == x:
            k += 1
            return k
        else:
            if x < li[midpoint]:
                return binSearch(li[:midpoint], x)
            else:
                return binSearch(li[midpoint + 1:], x)

ln1 = int(input())
b1 = []
for i in input().split(' '):
    b1.append(int(i))
ln2 = int(input())
b2 = []
for i in input().split(' '):
    b2.append(int(i))
ln3 = int(input())
b3 = []
for i in input().split(' '):
    b3.append(int(i))

l = 0
for i in b1:
    if binSearch(b2, i) == 1 and binSearch(b3, i) == 1:
        l += 1
    else:
        pass

print(l)
