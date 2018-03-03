#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1319. Hotel'''

# Dimension list n on n (empty)
def rangeList(num):
    alist = []
    str_ = []
    k = 1
    l = 1
    while k < num + 1:
        str_ = []
        while l < num*k + 1:
            str_.append(0)
            l += 1
        alist.append(list(str_))
        k += 1

    return alist

# Indices of the needed order
def values(num):
    alist = []
    alist_2 = []
    lst = []
    k = 0
    while k < num:
        lst.append(k)
        alist.append(list(lst))
        k += 1
    while k > 1:
        lst.pop(0)
        alist.append(list(lst))
        k -= 1

    for i in alist:
        item = reversed(i)
        alist_2.append(list(item))

    return alist, alist_2

# Input
n = int(input())

# Extracting values from nested lists into one list
lst1 = []
for i in values(n)[0]:
    for j in i:
        lst1.append(j)
lst2 = []
for i in values(n)[1]:
    for j in i:
        lst2.append(j)

# Main (arrangement of numbers in the needed order)
result = rangeList(n)[:]
k = 0
l = 1
while k < len(lst1):
    result[lst1[k]].pop(lst2[k])
    result[lst1[k]].insert(lst2[k], l)
    k += 1
    l += 1

# Otput
for i in result:
    print(*(reversed(i)))
