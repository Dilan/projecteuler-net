#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It was proposed by Christian Goldbach that every odd composite number
# can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1²
# 15 = 7 + 2×2²
# 21 = 3 + 2×3²
# 25 = 7 + 2×3²
# 27 = 19 + 2×2²
# 33 = 31 + 2×1²
# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot
# be written as the sum of a prime and twice a square?

def sieve_of_eratosthenes(limit):
    # create empty array
    list = [False, False] + map(lambda x: True, range(2, limit))

    for i, is_prime in enumerate(list):
        if is_prime:
            yield i

            for n in range(i*i, limit, i):
                list[n] = False

def sieve(limit):
    list = [False, False] + map(lambda x: True, range(2, limit))
    db = {}
    for i, is_prime in enumerate(list):
        if is_prime:
            yield (i, True)
            for n in range(i*i, limit, i):
                list[n] = False
        else:
            if i < 2:
                yield (i, None)
            elif i not in db:
                db[i] = True
                yield (i, False)

def can_sum_of_prime_and_twice_square(num, primes, debug=True):
    for n in range(0,num)[::-1]:
        # nearest primes:
        if n in primes:
            for i in range(1, 40):
                res = (2 * i**2) + n
                if res == num:
                    if debug:
                        print 'Found:', num, '=', n, '+', '2 ×', str(i) + '²'
                    return True
                if res > num:
                    break
    return False

def solution():
    answer = None
    primes = {}
    for item in sieve(10000):
        is_prime = (item[1] is True)
        is_composite = (item[1] is False)
        num = item[0]

        if is_prime:
            primes[num] = True

        if is_composite and num % 2:
            if not can_sum_of_prime_and_twice_square(num, primes, False):
                answer = num
                break

    return answer

def test():
    # generate primes:
    primes = {}
    for num in sieve_of_eratosthenes(2000):
        primes[num] = True

    # test case 1
    can_sum_of_prime_and_twice_square(1415, primes, True)

# test()

print 'Answer is:', solution()