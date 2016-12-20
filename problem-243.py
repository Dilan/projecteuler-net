# A positive fraction whose numerator is less than its denominator is called a proper fraction.
# For any denominator, d, there will be d-1 proper fractions
# for example, with d=12
# 1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12

# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), to be the 
# ratio of its proper fractions that are resilient; for example, R(12) = 4/11
# ------------------------------------------------------------------------------
# 1/12, 5/12, 7/12, 11/12, so just these fractions could not be cancelled down
# ------------------------------------------------------------------------------
# In fact d = 12 is the smallest denominator having a resilience R(d) < 4/10

# Find the smallest denominator d, having a resilience R(d) < 15499/94744 ~ 0.163588195559

# for  d = (2*3*5*7*11*13*17*19*23) R(d) 36495360/223092869 (0.163588196089)
#                                                            0.163588195559

import time
import math
ti=time.time()

primes = [2,3,5,7,11,13,17,19,23,29]
RESULT = 15499./94744.

def factorize(n):
    factors = []
    for p in primes:
        if p*p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            factors.append((p, i));
    if n > 1: factors.append((n, 1))
    return factors

# https://en.wikipedia.org/wiki/Euler's_totient_function
def euler_totient_function(n):
    s = n
    for item in factorize(n):
        s *= (1. - 1./item[0]) 
    return s

def R(d):
    return euler_totient_function(d) / (d - 1)

def next(base, pows):
    while pows[len(pows)-1] <= base:
        pows[0] += 1
        
        for i in range(0, len(pows)-1):
            if pows[i] > base:
                pows[i] = 1
                pows[i+1] += 1
        yield pows

def solution():
    for pows in next(4, [1] * (len(primes) - 1)):
        d = 1.
        for idx, p in enumerate(pows):
            d *= primes[idx] ** p

        if R(d) < RESULT:
            return d

    return None

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'
