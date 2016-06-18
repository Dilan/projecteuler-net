# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 x 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def permutation(list):
    if len(list) == 1:
        return [list]
    result = []
    for p in permutation(list[1:]):
        for i in range(len(p)+1):
            result.append(p[:i] + [list[0]] + p[i:])
    return result

def combination(elements, length):
    if length == 1:
        return map(lambda x: [x], elements)
    res = []
    for idx, element in enumerate(elements):
        for next in combination(elements[idx+1:], length-1):
            res.append([element] + next)
    return res

def to_num(list):
    return int(''.join(map(lambda x: str(x), list)))

def diff(a, b):
    return list(set(b).difference(a))

def is_pandigital(number, size):
    digits = range(1, size)
    number_list = map(lambda x: int(x), list(str(number)))
    number_list.sort()
    return number_list == digits

def find_pandigital(digits, multiplicand_size, multiplier_size):
    pandigitals = []

    combinations = combination(digits, multiplicand_size)
    for unique_combination in combinations:

        for variant in permutation(unique_combination):
            multiplicand = to_num(variant)

            multiplier_variants = []
            for x in combination(diff(variant, digits), multiplier_size):
                multiplier_variants.extend(permutation(x))

            for multiplier_list in multiplier_variants:
                multiplier = to_num(multiplier_list)

                product = multiplier * multiplicand

                if is_pandigital(int(str(product) + str(multiplier) + str(multiplicand)), len(digits)+1):
                    pandigitals.append((product, multiplicand, multiplier))

    return pandigitals

def solve(digits, variants):
    unique_pandigitals = {}

    for variant in variants:
        multiplicand_size = variant[0]
        multiplier_size = variant[1]

        pandigitals = find_pandigital(digits, multiplicand_size, multiplier_size)

        # print pandigitals

        for item in pandigitals:
            if item[0] not in unique_pandigitals:
                unique_pandigitals[item[0]] = True

    return sum(unique_pandigitals.keys())


# we have to check only: ==============================================
print solve(
    # map(lambda x: str(x),range(1,10)),
    range(1,10),
    [
        [1,3], # [x] * [xxx]
        [1,4], # [x] * [xxxx]
        [2,3]  # [xx] * [xxx]
    ]
)

# answer is 45228
