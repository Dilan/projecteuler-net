# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.
#
# Let d(1) be the 1st digit, d(2) be the 2nd digit, and so on. In this way, we note the following:
#
# d(2)d(3)d(4)  = 406 is divisible by 2
# d(3)d(4)d(5)  = 063 is divisible by 3
# d(4)d(5)d(6)  = 635 is divisible by 5
# d(5)d(6)d(7)  = 357 is divisible by 7
# d(6)d(7)d(8)  = 572 is divisible by 11
# d(7)d(8)d(9)  = 728 is divisible by 13
# d(8)d(9)d(10) = 289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools
import time

ti=time.time()

def permutations(l, size):
    return map(
        lambda x: ''.join(map(lambda i: str(i), list(x))),
        itertools.permutations(l, size))

def is_divisible(num, d):
    return float(num) % d == 0

def even_numbers(list, size):
    return filter(lambda x: int(x)%2 == 0, permutations(list, size))

def to_digits_list(num):
    return [int(n) for n in str(num)]

def diff(a, b):
    return list(set(b).difference(a))

# ======================
# steps: split into sub-lists with conditions:
# 1th could not be 0
# 4th always even
# so 6th always 5 or 0

def solution():
    origilal_list = range(0,10)

    numbers_2_4 = even_numbers(origilal_list, 3) # all even numbers 3 digits length
    numbers_2_6 = []
    for num_2_4 in numbers_2_4:
        rest = diff(to_digits_list(num_2_4), origilal_list)

        # '346' -> rest [0,1,2,5, ...] ==>  [1,2,5,6 ...] or [0,1,2,6 ...]
        for num_6 in [0,5]:
            if num_6 not in rest:
                continue
            num_5_list = diff([num_6], rest)
            for num_5 in num_5_list:
                num_3_5 = num_2_4[1:] + str(num_5)
                if is_divisible(num_3_5, 3):
                    numbers_2_6.append(num_2_4[0] + num_3_5 + str(num_6))

    numbers_2_10 = []
    for num_2_6 in numbers_2_6:
        rest = diff(to_digits_list(num_2_6), origilal_list)

        numbers_7_10 = permutations(rest, 4)
        for num_7_10 in numbers_7_10:
            num_5_7 = num_2_6[-2:] + num_7_10[0] #is divisible by 7
            num_6_8 = num_2_6[-1] + num_7_10[0:2] # is divisible by 11
            num_7_9 = num_7_10[0:3] # is divisible by 13
            num_8_10 = num_7_10[1:] # is divisible by 17

            divisible_condition = True
            for options in [[num_8_10, 17], [num_7_9, 13], [num_6_8, 11], [num_5_7, 7]]:
                if not is_divisible(options[0], options[1]):
                    divisible_condition = False
                    break
            if divisible_condition:
                numbers_2_10.append(num_2_6 + num_7_10)

    result = []
    for num_2_10 in numbers_2_10:
        # 1st number could not be zero
        rest = diff(to_digits_list(num_2_10), origilal_list)
        if rest[0] > 0:
            result.append(int(str(rest[0]) + num_2_10))

    return sum(result)

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'
