#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1044. Lucky Tickets'''

import math


def tickets(num):
    tickets = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
    for i in range(10, int(math.pow(10, int(num / 2)))):
        tickets.append(str(i))

    return tickets

def sumTicket(alist):
    numbers = []
    for i in tickets(n):
        sumJ = 0
        for j in i:
            sumJ += int(j)
        numbers.append(sumJ)

    numbers = sorted(numbers)

    return numbers

def main(num):
    lst = []
    values = sumTicket(tickets(num))
    k = 1
    m = values[0]
    for i in values[1:]:
        if m == i:
            k += 1
            m = i
        else:
            lst.append(k)
            k = 1
            m = i

    if values[len(values) - 2] != values[len(values) - 1]:
        lst.append(1)

    nums = 0
    for i in lst:
        nums += math.pow(i, 2)

    return int(nums)


n = int(input())
print(main(n))
