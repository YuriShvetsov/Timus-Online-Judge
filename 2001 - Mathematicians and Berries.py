#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''2001. Mathematicians and Berries'''

import sys

a = []

for line in sys.stdin:
    for i in line.split():
        a.append(int(i))

print((a[0] - a[4]), (a[1] - a[3]))
