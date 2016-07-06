#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
# 8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
# 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
# As 1 = 1⁴ is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def is_any_magic(num, power):
    res = 0
    for digit in str(num):
        digit = int(digit)
        res += digit**power
    return res == num

result = 0
for num in range(100, 500000): # no need to calculate over this number
    if is_any_magic(num, 5):
        result+= num

print 'Answer is:', result