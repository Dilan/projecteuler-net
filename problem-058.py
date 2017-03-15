# -*- coding: utf-8 -*-

# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, 
# but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
# that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, 
# a square spiral with side length 9 will be formed. 
# If this process is continued, what is the side length of the square spiral 
# for which the ratio of primes along both diagonals first falls below 10%?

import numpy
import time
ti=time.time()

def prime_list(n):
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def build_primes(limit):
    hm = { }
    for prime in prime_list(limit):
        hm[int(prime)] = True
    return hm

def solution():
    primes = build_primes(800000000)
    
    total_in_diagonals = 1
    primes_in_diagonals = 0
    last_num = 1
    side = 1
    ratio = 1.0
    
    while float(ratio) >= float(1.0/10.0):
        corner_1 = last_num + (side + 1)
        corner_2 = corner_1 + (side + 1)
        corner_3 = corner_2 + (side + 1)
        last_num = corner_3 + (side + 1)
        
        total_in_diagonals += 4
        side += 2
        
        if corner_1 in primes:
            primes_in_diagonals += 1
        if corner_2 in primes:
            primes_in_diagonals += 1
        if corner_3 in primes:
            primes_in_diagonals += 1
        if last_num in primes:
            primes_in_diagonals += 1
        
        ratio = float(primes_in_diagonals)/float(total_in_diagonals)

    # print 'ratio:', ratio, primes_in_diagonals, '/', total_in_diagonals
    # print 'last_num:', last_num

    return side

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'