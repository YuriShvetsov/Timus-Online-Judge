#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1545. Hieroglyphs'''

import sys


n = int(input())
hs = []
for line in sys.stdin:
    hs.append(line[:-1])

vova = hs[len(hs) - 1]

hs.pop(len(hs) - 1)
hs = sorted(hs)

for i in hs:
    if i[0] == vova:
        print(i)
    else:
        pass
