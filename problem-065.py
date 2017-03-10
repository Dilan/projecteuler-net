# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]

import time
ti=time.time()

def get_fraction(a, b, c): # a + b/c
    # print a, '+', b, '/', c, ' = ', (c * a + b), '/', c
    return ((c * a + b), c)

def generate_sequence(length):
    items = [2]
    length -= 1
    k = 2
    while length > 0:
        for idx, i in enumerate([1,0,1]):
            if length == 0:
                break
            if idx == 1:
                i += k
            items.append(i)
            length -= 1
        k += 2
    return items

def solution(length):
    sequence = generate_sequence(length)
    idx = len(sequence) - 2
    prev = (sequence[-1], 1)

    while idx > 0:  
        prev = get_fraction(sequence[idx], prev[1], prev[0])
        idx -= 1

    prev = get_fraction(sequence[0], prev[1], prev[0])
    
    return reduce(lambda x,y: int(x)+int(y), list(str(prev[0])))

print 'Answer is:', solution(100), '(time:', (time.time()-ti), ')'
