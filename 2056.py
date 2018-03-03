#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''2056. Scholarship'''

import math
import sys


n = int(input())
assessments = []
for line in sys.stdin:
    assessments.append(int(line[:-1]))

check = ''
for i in assessments:
    if i == 3:
        check = 'None'
        break

if check == 'None':
    print(check)
elif sum(assessments) == n * 5:
    print('Named')
elif sum(assessments) / n >= 4.5:
    print('High')
else:
    print('Common')
