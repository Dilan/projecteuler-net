#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It is possible to show that the square root of two can be expressed as an infinite continued fraction.

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, 
# but the eighth expansion, 1393/985, is the first example where 
# the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

import time
ti=time.time()

def sum_up(a, fraction): # a + b/c
    # print a, '+', b, '/', c, ' = ', (c * a + b), '/', c
    b = fraction[0]
    c = fraction[1]
    return ((c * a + b), c)

def plus1(fraction): # a + b/c
    return sum_up(1, fraction)

def swap(fraction): # a + b/c
    return (fraction[1], fraction[0])

def is_length_different(x, y):
    return len(str(x)) != len(str(y))

def solution(length):
    counter = 0
    prev = (3, 2)

    while length > 0:
        # 1 + 1 / (prev)
        prev = sum_up(1, swap(plus1(prev)))
        if is_length_different(prev[0], prev[1]):
            counter += 1
        length -= 1
    return counter

print 'Answer is:', solution(1000), '(time:', (time.time()-ti), ')'
