# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

# 197 -> 971 -> 719
def circulars(num, counter=0):
    if counter == len(str(num)):
        return []
    shifted_num = int(str(num)[1:] + str(num)[0])
    return [shifted_num] +  circulars(shifted_num, counter+1)

def has_digits(number, digits):
    for digit in str(number):
        if int(digit) in digits:
            return True
    return False

def might_be_circular_prime(num):
    return False if num > 9 and has_digits(num, [0,2,4,5,6,8]) else True

def is_circular_prime(num, list):
    numbers = circulars(num)
    for n in numbers:
        if n not in list:
            return False
    return True

def sieve_of_eratosthenes(limit):
    # create empty array
    list = [False, False] + map(lambda x: True, range(2, limit))

    for i, is_prime in enumerate(list):
        if is_prime:
            yield i

            for n in range(i*i, limit, i):
                list[n] = False

# =======================================================

prime_numbers = list(sieve_of_eratosthenes(1000000))
# exclude number with even digits and 5 (could not be circular prime)
filtered_numbers = filter(might_be_circular_prime, prime_numbers)
circular_primes = filter(lambda x: is_circular_prime(x, filtered_numbers), filtered_numbers)

# print circular_primes
print 'Answer:', len(circular_primes), 'circular primes' # 55
