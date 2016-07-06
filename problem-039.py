#!/usr/bin/env python
# -*- coding: utf-8 -*-

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?
import math

# so range might be following:
# p/2 < hypotenuse < (p - 2 * p/(2+√2))

result = [0,0]
p = 10
while p <= 1000:
    tmp_result = [p,0]

    max = int(p/2)
    min = int(math.ceil((p - 2 * p/(2 + 2**(0.5)))))

    # hypotenuse
    for c in range(min, max):
        # print c
        a_min = int(math.ceil(c/2**(0.5)))
        a_max = int(p/2)
        for a in range(a_min, a_max):
            b = p - c - a
            if (b**2 + a**2) == c**2:
                tmp_result[1] += 1
                # print 'p=', p, ' in {', a,',',b,',',c,'}'

    if tmp_result[1] > result[1]:
        result[0] = tmp_result[0]
        result[1] = tmp_result[1]

    p += 2

print 'Answer is:', result[0]
