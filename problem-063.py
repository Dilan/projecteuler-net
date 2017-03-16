# The 5-digit number, 16807=7^5, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

import time
import math
ti=time.time()

def solution():
    n = 2
    p = 1
    counter = 1 # (1^1)

    while n < 10:
        value = int(math.pow(n,p))
        l = len(str(value))
        
        if l == p:
            # print n, '^', p, '=', value, 'is', (str(p)+'th'), 'power'
            counter += 1
        else:
            p = 0
            n += 1
        p += 1 # more power!

    return counter

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'
