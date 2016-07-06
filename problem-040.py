#!/usr/bin/env python
# -*- coding: utf-8 -*-

# An irrational decimal fraction is created by concatenating the positive integers:
# 0.12345678910[1]112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

d = 1
num = 1
length = 0
result = []

while d <= 1000000:
    num_str = str(num)
    length += len(num_str)

    if d <= length:
        # print 'num:', num_str
        # print num_str[(d - length - 1)]
        result.append(int(num_str[(d - length - 1)]))
        d *= 10
    num += 1

print 'Answer is:', reduce(lambda x,y: x*y, result)
