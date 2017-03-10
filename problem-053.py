#!/usr/bin/env python
# -*- coding: utf-8 -*-

# There are exactly ten ways of selecting three from five, 12345:
#    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, 5C3 = 10.

# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

import math
import time
ti=time.time()

def C(r, n):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

def solution():
    counter = 0
    for n in range(1,101):
        r = 1
        while (n >= r):
            result = C(r,n)
            if result > 1000000:
                counter += 1
            r += 1
    return counter

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'
