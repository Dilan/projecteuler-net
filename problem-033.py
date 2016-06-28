# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
# it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from fractions import gcd

# exclude 10,20, ...
# exclude 11,22, ...
def two_digits_numbers(start=10):
    list = filter(lambda x: x%10, range(start,100))
    list = filter(lambda x: x not in [11,22,33,44,55,66,77,88,99], list)
    return list

def is_curious_fraction(numerator, denominator):
    cleaned_numerator = str(numerator)
    cleaned_denominator = str(denominator)

    for digit in str(cleaned_numerator):
        if digit in cleaned_denominator:
            cleaned_numerator = cleaned_numerator.replace(digit, '', 1)
            cleaned_denominator = cleaned_denominator.replace(digit, '', 1)

    if len(cleaned_numerator) == 0 or len(cleaned_denominator) == 0:
        return False

    return (float(cleaned_numerator) / float(cleaned_denominator)) == (float(numerator) / float(denominator))

# for 2 digits number only
def potential_option(value):
    digit_1 = int(str(value)[0])
    digit_2 = int(str(value)[1])

    list = []
    for num in two_digits_numbers(value+1):
        num_1 = int(str(num)[0])
        num_2 = int(str(num)[1])

        if digit_1 in [num_1, num_2] and digit_2 in [num_1, num_2]:
            continue
        elif digit_1 in [num_1, num_2] or digit_2 in [num_1, num_2]:
            list.append(num)

    return list

# =================================================
numerator_product = 1
denominator_product = 1

for num in two_digits_numbers():
    for denominator in potential_option(num):
        if is_curious_fraction(num, denominator):
            print num, '/', denominator
            numerator_product *= num
            denominator_product *= denominator

# find lowest common terms
while True:
    greatest_common_divisor = gcd(denominator_product, numerator_product)
    if greatest_common_divisor == 1:
        break
    numerator_product = numerator_product / greatest_common_divisor
    denominator_product = denominator_product / greatest_common_divisor

print '================'
print 'Answer is',  denominator_product
