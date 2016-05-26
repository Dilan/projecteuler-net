# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

one_to_nine = { 0: 1, 1: 1 }

for num in range(2,10):
    one_to_nine[num] = num * one_to_nine[num - 1]

numbers = []
for n in range(3,100000):
    splited = map(lambda x: int(x), list(str(n)))

    l = map(lambda x: one_to_nine[x], splited)

    if sum(l) == n:
        numbers.append(n)

print numbers
print '-------------\nanswer is:', sum(numbers)
