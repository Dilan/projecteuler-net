# By replacing the 1st digit of the 2-digit number *3, 
# it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

 # By replacing the 3rd and 4th digits of 56**3 with the same digit, 
 # this 5-digit number is the first example having seven primes among the ten generated numbers, 
 # yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
 # Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number 
# (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import time
ti=time.time()

def primes(limit):
    list = [False, False] + map(lambda x: True, range(2, limit))
    for i, is_prime in enumerate(list):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):
                list[n] = False

class Num():
    val = None
    arr = None
    size = None
    def __init__(self, val):
        self.val = val
        self.arr = list(str(val))
        self.size = len(self.arr)
    
class Statistics():
    storage = {}
    
    def to_storage(self, mask, num):
        if mask in self.storage:
            self.storage[mask]["counter"] += 1
            self.storage[mask]["items"].append(num)
        else:
            self.storage[mask] = { "counter": 1, "items": [num] }
    
    def add(self, num, n=0, digit=None, mask=None):
        if mask is None:
            mask = num.arr[:]
        
        for i in range(n, num.size-1):
            if  n == 0 or digit == num.arr[i]:
                mask[i] = '*'
                self.to_storage(''.join(mask), num.val)
                
                if (i+1) < num.size:
                    self.add(num, i+1, num.arr[i], mask)
                
                mask[i] = num.arr[i]
    
def solution():
    stat = Statistics()
    
    for prime in primes(1000000):
        stat.add(Num(prime))
    
    for k in stat.storage:
        if stat.storage[k]['counter'] == 8:
            return stat.storage[k]['items'][0]
    return None

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'
