#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1149. Sinus Dances'''

def An(num):
    sin = 'sin('
    k = 1
    while k < num:
        if k % 2 != 0:
            sin += str(k) + '-sin('
        else:
            sin += str(k) + '+sin('
        k += 1

    if num % 2 != 0:
        sin += str(num) + ')'*num
    else:
        sin += str(num) + ')'*num

    return sin

def Sn(num):
    result = '('*(num - 1)
    k = 1
    while k < num:
        result += str(An(k)) + '+' + str(num + 1 - k) + ')'
        k += 1

    result += str(An(num)) + '+1'

    return result


n = int(input())

print(Sn(n))
