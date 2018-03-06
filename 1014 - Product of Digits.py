#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1014. Product of Digits'''

n = int(input())

def main(num):
    alist = []

    if num == 0:
        alist.append(10)
    else:
        while len(str(num)) > 1:
            k = 9
            while num % k != 0:
                k -= 1

                if k == 1:
                    return -1
            alist.append(k)
            num = int(num / k)

        alist.append(num)
        alist = sorted(alist)

    return alist

def secondary(num):
    astr = ''

    if main(num) == -1:
        return -1
    else:
        for j in main(num):
            astr += str(j)

        return int(astr)


print(secondary(n))
