# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
#  (1,2, ... , n) where n > 1?

def is_pandigital(number, size=9):
    digits = range(1, size+1)
    number_list = map(lambda x: int(x), list(str(number)))
    number_list.sort()
    return number_list == digits

def might_be_pandigital(num, size=9):
    used = []
    available = range(1,size+1)

    for digit in str(num):
        digit = int(digit)
        if digit in used or digit not in available:
            return False
        used.append(digit)
        available.remove(digit)
    return True

# ===========================================
pandigital = 0
n = 1
while n < 100000:
    result = ''
    for digit in range(1,6):
        result += str(digit * n)
        if not might_be_pandigital(int(result)):
            break
        if len(result) == 9 and is_pandigital(int(result)):
            # print 'pandigital =', result
            # print 'n =', n
            # print 'digit from 1 to ', digit
            if pandigital < int(result):
                pandigital = int(result)
    n += 1

print 'Answer is:', pandigital