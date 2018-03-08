#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1001. Reverse root'''

a = []
for line in sys.stdin:
    for i in line.split():
        a.append(int(i))

a = reversed(a)
x = 1/2

for i in a:
    print( '%.4f' % (i ** x) )
