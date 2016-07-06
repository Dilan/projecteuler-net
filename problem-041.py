#!/usr/bin/env python
# -*- coding: utf-8 -*-

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

def is_pandigital(number, size):
    digits = range(1, size+1)
    number_list = map(lambda x: int(x), list(str(number)))
    number_list.sort()
    return number_list == digits

def sieve_of_eratosthenes(limit):
    # create empty array
    list = [False, False] + map(lambda x: True, range(2, limit))

    for i, is_prime in enumerate(list):
        if is_prime:
            yield i

            for n in range(i*i, limit, i):
                list[n] = False

# 9n exclude 'coz --> (1+2+3+4+5+6+7+8+9=45 => dividable by 3)
# 8n exclude 'coz --> (1+2+3+4+5+6+7+8=36 => dividable by 3)

limit = 7654321
prime_numbers = list(sieve_of_eratosthenes(limit))

for num in prime_numbers[::-1]:
    if is_pandigital(num, len(str(num))):
        print 'Answer is:', num
        break
