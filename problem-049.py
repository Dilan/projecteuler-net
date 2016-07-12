#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
# is unusual in two ways: 
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

import itertools

def suggestion(num):
	l = filter(
		lambda x: len(str(x)) == len(str(num)),
		map(
			lambda x: int(''.join(map(lambda i: str(i), list(x)))),
			itertools.permutations(list(str(num)))
		)
	)
	result = []
	for i in l:
		if i > num and i not in result and i%2:
			result.append(i)
	result.sort()
	return result

def is_increase_with_equal_step(list):
	step = list[1]-list[0]
	for idx, num in enumerate(list[2:]):
		idx += 2
		if num - list[idx-1] != step:
			return False
	return True

def sieve_of_eratosthenes(limit):
	list = [False,False] + [True for i in range(2,limit)]
	for i, is_prime in enumerate(list):
		if is_prime:
			yield i
			for i in range(i*i, limit, i):
				list[i] = 0

def is_all_primes(list, primes):
	for num in list:
		if num not in primes:
			return False
	return True

def solve():
	# 1) get 4 digits primes only
	four_digits_primes = filter(
		lambda x: len(str(x)) == 4,
		list(sieve_of_eratosthenes(10000))
	)

	# 2) for each prime generate prime permutations
	filtered_list = []
	for num in four_digits_primes:
		variants = suggestion(num)
		if len(variants) > 1:
			variants = filter(lambda x: x in four_digits_primes, variants)

			if len(variants) > 1:
				filtered_list.append([num] + variants)

	# 3) trying to find increasing sequence
	for l in filtered_list:
		if len(l) == 3:
			if is_increase_with_equal_step(l):
				# funny, but it was found in 3 length list :)
				return l

print solve()