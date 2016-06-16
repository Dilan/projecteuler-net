# Double-base palindromes
# =======================
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_polindromic(value):
    for idx in range(len(value)/2):
        if value[idx] != value[-(idx+1)]:
            return False
    return True

def reverse(num):
    return str(num)[::-1]

def split_num(number):
    length = len(number)
    left = number[:length/2]
    middle = int(number[length/2]) if length % 2 else None
    right = number[length/2+1:] if length % 2 else number[length/2:]

    return (int(left), middle, int(right))

def next_polindromic_number(num):
    l, m, r = split_num(str(num+1))

    if m is None:
        if int(reverse(l)) >= r:
            return int(str(l) + reverse(l))
        else:
            return int(str(l+1) + reverse(l+1))
    else:
        if int(reverse(l)) >= r:
            return int(str(l) + str(m) + reverse(l))
        else:
            if m < 9:
                return int(str(l) + str(m+1) + reverse(l))
            else:
                return int(str(l+1) + str(0) + reverse(l+1))

def to_binary(dec):
    return bin(dec)[2:]

# ===========================================
sum = 0
n = 0
while(n < 1000000):
    if n < 10:
        if is_polindromic(to_binary(n)):
            sum += n
        n += 1
    else:
        dec = next_polindromic_number(n)
        if is_polindromic(to_binary(dec)):
            sum += dec
            # print dec
            # print to_binary(dec)
        n = dec

print sum # 872187
