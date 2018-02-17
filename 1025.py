#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1025. Democracy in danger'''

import sys, math

x = []

for line in sys.stdin:
   for i in line.split():
      x.append(float(i))

x.reverse()

for i in x:
   print("%.4f" % math.sqrt(i))
