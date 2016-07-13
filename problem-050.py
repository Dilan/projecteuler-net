#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def sieve_of_eratosthenes(limit):
    list = [False,False] + [True for i in range(2,limit)]
    for i, is_prime in enumerate(list):
        if is_prime:
            yield i
            for i in range(i*i, limit, i):
                list[i] = 0

# consecutive_primes_sum
# [5, 7, 11, 13]:
# (5, 5+7, 5+7+11, 5+7+11+13)
# (     7,   7+11,   7+11+13)
# (            11,     11+13)
# (                       13)
def consecutive_sums(l):
    result = {}
    prev = []
    for num in l:
        tail = prev[:]
        prev = [num]
        result[num] = 1
        for i, x in enumerate(tail):
            result[num + x] = i + 2
            prev.append(num + x)
    return result

def solve():
    prime_numbers = list(sieve_of_eratosthenes(1000000))
    sums = consecutive_sums(prime_numbers[0:550]) # max sum ~ 1.000.000

    answer = None
    max_sequence = 0
    for num in prime_numbers[::-1]:
        if num < 100000:
            break
        if num in sums:
            if max_sequence < sums[num]:
                max_sequence = sums[num]
                answer = num
    return answer

print solve()