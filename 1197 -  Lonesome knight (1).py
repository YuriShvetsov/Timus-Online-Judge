#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1197. Lonesome knight'''

import sys

n = int(input())
tests = []
for line in sys.stdin:
    for i in line.split():
        tests.append(i)

two = ['a1', 'a8', 'h1', 'h8']
three = ['b1', 'g1', 'a2', 'h2', 'a7', 'h7', 'b8', 'g8']
four = ['a3', 'c1', 'f1', 'h3', 'a6', 'c8', 'f8', 'h6', 'd1', 'e1', 'a4', 'a5', 'd8', 'e8', 'h4', 'h5', 'b2', 'b7', 'g2', 'g7']
six = ['b3', 'c2', 'b6', 'c7', 'f2', 'g3', 'g6', 'f7', 'd2', 'e2', 'b4', 'b5', 'd7', 'e7', 'g4', 'g5']
eight = ['c3', 'c4', 'c5', 'c6', 'd3', 'd4', 'd5', 'd6', 'e3', 'e4', 'e5', 'e6', 'f3', 'f4', 'f5', 'f6']

for item in tests:
    for i2 in two:
        if item == i2:
            print('2')
        else:
            pass

    for i3 in three:
        if item == i3:
            print('3')
        else:
            pass

    for i4 in four:
        if item == i4:
            print('4')
        else:
            pass

    for i6 in six:
        if item == i6:
            print('6')
        else:
            pass

    for i8 in eight:
        if item == i8:
            print('8')
        else:
            pass
