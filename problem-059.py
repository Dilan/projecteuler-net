# Each character on a computer is assigned a unique code and the preferred 
# standard is ASCII (American Standard Code for Information Interchange). 
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, 
# then XOR each byte with a given value, taken from a secret key. 
# The advantage with the XOR function is that using the same encryption key on 
# the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, 
# and the key is made up of random bytes. 
# The user would keep the encrypted message and the encryption key in different 
# locations, and without both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method 
# is to use a password as a key. If the password is shorter than the message, 
# which is likely, the key is repeated cyclically throughout the message. 
# The balance for this method is using a sufficiently long password key for security, 
# but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters. 
# Using cipher.txt file containing the encrypted ASCII codes, and the knowledge that 
# the plain text must contain common English words, decrypt the message and find 
# the sum of the ASCII values in the original text.

import time
ti=time.time()

def read_data_from_file(file_path):
    f = open(file_path, 'r')
    items = f.read().strip().split(',')
    return [int(item) for item in items]

def to_ord(str):
    return [ord(x) for x in str]

def to_chr(codes):
    return ''.join([chr(x) for x in codes])

def to_str(items):
    return ''.join([str(item) for item in items])

def decrypt(key, codes):
    result = []
    for idx, code in enumerate(codes):
        k = idx % len(key)
        result.append(key[k]^code)
    return result

def generate_keys(items, length):
    if length == 1:
        return [[x] for x in items]
    
    result = []
    seen = {}
    pk = generate_keys(items, length-1)
    
    for l in items:
        for p in pk:
            for i in range(0,length):
                item = p[:i] + [l] + p[i:]
                s = to_str(item)
                if s not in seen:
                    seen[s] = True
                    result.append(p[:i] + [l] + p[i:])
    return result

def solution():
    codes = read_data_from_file('data/p059_cipher.txt')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # generate all available encryption keys (length = 3)
    all_keys = generate_keys(to_ord(alphabet), 3)
    possible_keys = []
    
    for key in all_keys:
        decripted = decrypt(key, codes)
        
        # calculate spaces (" ")
        spaces = 0
        for k in decripted:
            if k == 32:
                spaces += 1
        
        if spaces >= 200 and spaces <= 600:
            possible_keys.append((key, decripted))

    if len(possible_keys) == 1:
        key = to_chr(possible_keys[0][0])
        decripted = possible_keys[0][1]
        decripted_sum = reduce(lambda a,b: a+b, decripted, 0)
        return str(decripted_sum) + '\n' + to_chr(decripted) + '\n'
    else:
        return '[Frequency analysis required]'

print 'Answer is:', solution(), '(time:', (time.time()-ti), ')'