#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1014. Product of Digits'''

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
                    return False
            alist.append(k)
            num = int(num / k)

        alist.append(num)
        alist = sorted(alist)

    return alist

def secondary(num):
    astr = ''

    if not main(num):
        return -1
    else:
        for j in main(num):
            astr += str(j)

        return int(astr)


n = int(input())

print(secondary(n))
