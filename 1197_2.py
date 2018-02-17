#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1197. Lonesome knight'''

import sys

n = int(input())
tests = []
for line in sys.stdin:
    for i in line.split():
        tests.append(i)

for i in tests:
    x = i[0]; y = int(i[1])
    if (x == 'a' or x == 'h') and (y == 1 or y == 8):
        print('2')

    elif (x == 'b' or x == 'g') and (y == 1 or y == 8):
        print('3')
    elif (x == 'a' or x == 'h') and (y == 2 or y == 7):
        print('3')

    elif (x == 'a' or x == 'h') and (y == 3 or y == 6):
        print('4')
    elif (x == 'c' or x == 'f') and (y == 1 or y == 8):
        print('4')
    elif (x == 'd' or x == 'e') and (y == 1 or y == 8):
        print('4')
    elif (x == 'a' or x == 'h') and (y == 4 or y == 5):
        print('4')
    elif (x == 'b' or x == 'g') and (y == 2 or y == 7):
        print('4')

    elif (x == 'b' or x == 'g') and (y == 3 or y == 6):
        print('6')
    elif (x == 'c' or x == 'f') and (y == 2 or y == 7):
        print('6')
    elif (x == 'd' or x == 'e') and (y == 2 or y == 7):
        print('6')
    elif (x == 'b' or x == 'g') and (y == 4 or y == 5):
        print('6')

    else:
        print('8')
