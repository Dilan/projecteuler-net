# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least two positive integers?

import time
import math
ti=time.time()

def digits_sum(digits): # used for test only
    limit = len(digits) + 1
    result = 0
    for idx, num in enumerate(digits):
        x = len(digits) - idx
        result += num * x
    return result

def owerflow_bits(digits, limit, num, base):
    _sum = limit
    
    for i in range(len(digits)-1, 0, -1):
        _sum -= ((digits[i]-1) * num[i])
        
        digits[i] = 0
        digits[i-1] += 1
        
        _sum += (num[i-1])
        _sum -= num[i]
        
        if _sum <= limit:
            break
    
    if _sum == limit:
        _sum -= 1
        digits[-1] -= 1
    
    return _sum

def next(digits, limit, num, base):
    _sum = 0

    while(digits[0] <= 1):
        digits[-1] += 1
        _sum += 1

        if digits[-1] > base[-1]:
            for i in range(len(digits)-1, 0, -1):
                if digits[i] > base[i]: # shift to next rank on overflow
                    _sum -= ((digits[i]-1) * num[i])
                    
                    digits[i] = 0
                    digits[i-1] += 1
                    
                    _sum += (num[i-1])
                    _sum -= num[i]
                else:
                    break # no need to analyze anymore
        
        if _sum == limit:
            # print '[', _sum, ']', digits
            yield digits
            # shift to avoid useless calculation
            _sum = owerflow_bits(digits, limit, num, base)

def solution(limit):
    digits = [0] * (limit-1) # default: [ 0, 0, 0 .... ]
    num = [0] * (limit-1)
    base = [0] * (limit-1)

    for i in range(len(digits)-1, -1, -1):
        x = limit - (i + 1)
        base[i] = int(math.ceil(limit/x))
        num[i] = x

    # i.e. for limit = 6
    # num    5 | 4 | 3 | 2 | 1 |
    # --------------------------
    # base   1 | 1 | 2 | 4 | 6 |

    counter = 0
    for d in next(digits, limit, num, base):
        counter += 1
    return counter

print 'Answer is:', solution(100), '(time:', (time.time()-ti), ')'
