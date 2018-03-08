#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1086. Cryptography'''

import sys


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def listPrimeNumbers(n):
    lst = [2]
    for i in range(3, n + 1, 2):
        if isPrime(i) == True:
            lst.append(i)

    return lst

lp = listPrimeNumbers(163842)

numbers = []
for line in sys.stdin:
    for i in line.split():
        numbers.append(int(i))

for i in numbers[1:]:
    print(lp[i - 1])
