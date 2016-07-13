#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?

import time
ti=time.time()

def sieve_of_eratosthenes(limit):
    list = [False, False] + map(lambda x: True, range(2, limit))

    for i, is_prime in enumerate(list):
        if is_prime:
            yield i

            for n in range(i*i, limit, i):
                list[n] = False

def has_distinct_prime_factors(num, size, primes):
    result = {}
    i = 0
    p = primes[i]
    while p <= num:
        if num % p == 0:
            result[p] = (result[p] + 1) if p in result else 1
            num = num / p
            if len(result.keys()) == size and num > 1:
                return False
        else:
            i += 1
            p = primes[i]

    return len(result.keys()) == size

def solution():
    primes = list(sieve_of_eratosthenes(1000000))
    counter = 0
    size = 4
    for num in range(1, 1000000):
        if has_distinct_prime_factors(num, size, primes):
            counter += 1
            if counter == size:
                return num - size + 1
        else:
            counter = 0

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'


