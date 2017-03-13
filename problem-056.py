#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A googol (10^100) is a massive number: one followed by one-hundred zeros; 
# 100^100 is almost unimaginably large: one followed by two-hundred zeros. 
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import math
import time
ti=time.time()

def count(a, b):
    return sum(map(int, str(pow(a, b))))

def solution():
    _max = 0
    for i in range(1,100):
        for j in range(1,100):
           res = count(i, j)
           if _max < res:
               _max = res
    return _max

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'
