# -*- coding: utf-8 -*-

# How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?

import time
import math
ti=time.time()

def next(digits, base, limit):
    while(digits[0] <= base):
        digits[-1] += 1;
        # shift to next rank on overflow
        for i in range(len(digits)-1, 0, -1):
            if digits[i] > base:
                digits[i] = 0
                digits[i-1] += 1
        if sum(digits) == limit:
            yield digits

def solution():
    f18 = math.factorial(18)
    result = 0
    digits = [0] * 10
    
    for d in next(digits, 3, 18):
        res = f18
        for num in d:
            res /= math.factorial(num)
        result += res

    return result * 9 / 10;

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'