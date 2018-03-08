#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1313. Some Words about Sport'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''1313. Some Words about Sport'''

import sys

n = int(input())

pixels = []
for line in sys.stdin:
    pixels.append(list(line[:-1].split(' ')))

k = 0
for line in pixels:
    while k < len(line):
        j = int(line[k])
        line.pop(k)
        line.insert(k, j)
        k += 1
    k = 0

c = 0
lst1 = []
lst2 = []

while c < n:
    lst1.append(c)
    lst2.append(list(lst1))
    c += 1

while len(lst1) != 1:
    lst1.pop(0)
    lst2.append(list(lst1))

lst3 = lst2[:]
k = 0
while k < len(lst2):
    lst4 = lst2[k][:]
    lst2.pop(k)
    lst4 = reversed(lst4)
    lst2.insert(k, list(lst4))
    k += 1

coub = []
k = 0; l = 0
for i in lst2:
    for j in i:
        coub.append(j)

coub2 = []
k = 0; l = 0
for i in lst3:
    for j in i:
        coub2.append(j)

result = []
k = 0

while k < len(coub):
    result.append(pixels[coub[k]][coub2[k]])
    k += 1

print(*result)
