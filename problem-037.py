# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def sieve_of_eratosthenes(limit):
    list = [False, False] + map(lambda x: True, range(2, limit))
    for i, is_prime in enumerate(list):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):
                list[n] = False

def has_digits(number, digits):
    for digit in str(number):
        if int(digit) in digits:
            return True
    return False

def slice_number(num):
    result = [num]
    for idx in range(1, len(str(num))):
        result.append(int(str(num)[idx:]))
    for idx in range(len(str(num))-1, 0, -1):
        result.append(int(str(num)[:idx]))
    return result

def is_truncatable_prime(num, list):
    if num < 10:
        return False

    for n in slice_number(num):
        if n not in list:
            return False
    return True

def might_be_truncatable_prime(num):
    if num < 100:
        return num
    else:
        # fist and last 2 digits
        start = int(str(num)[0:2])
        end = int(str(num)[-2:])

    return (start in [11, 13, 17, 19, 23, 29, 31, 37, 53, 59, 71, 73, 79] and
            end in [13, 17, 23, 37, 43, 47, 53, 67, 73, 79, 83, 97])

prime_numbers = list(sieve_of_eratosthenes(1000000))
filtered_numbers = filter(might_be_truncatable_prime, prime_numbers)
truncatable_primes = filter(lambda x: is_truncatable_prime(x, prime_numbers), filtered_numbers)
print 'Answer is:', sum(truncatable_primes)
