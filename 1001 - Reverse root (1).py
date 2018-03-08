#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1001. Reverse root'''

import math
import sys


a = []
for line in sys.stdin:
    for i in line.split():
        a.append(int(i))
        
a = reversed(a)

for i in a:
    print('%.4f' % math.sqrt(i))
