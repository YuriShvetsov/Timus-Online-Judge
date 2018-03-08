#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1086. Cryptography'''
# Оптимизировать функцию isPrime(n)

import math
import sys


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def listPrimeNumbers(n):
    lst = []
    for i in range(2, n + 1):
        if isPrime(i) == True:
            lst.append(i)

    return lst

lp = listPrimeNumbers(170000)

numbers = []
for line in sys.stdin:
    for i in line.split():
        numbers.append(int(i))

for i in numbers[1:]:
    print(lp[i - 1])
