# We have three keys: key1, key2, key3.
# key3 should be an integer

# Python's integer representation of characters in key1 and key2 are strung
# together to make two integers, and we calculate the modulus of each other and
# the modulus of moduli until a modulus is smaller than 1114111.

# We then combine key1 and key2, and string python's integer representation of
# those characters to make another integer, and we find that number mod 1031.
# We'll call this number the 'key'.

# Then, we take the result from the key1 and key2 moduli and use it as a seed
# to generate a number between[0, key], with python's random module, and save
# it to a list, which we'll call 'shifts', that we'll use later.

# We take the number generated from the seed and put it to the 'key'-th
# exponent, and we then mod this by key3, to then put into python's random
# module as a seed and generate more random numbers. We keep going until the
# 'shifts' list is the same length as the message.

# Then we shift each character in the message by the number of shifts in the
# shifts list, on a randomized dial that's unique and stored in the code.

# The decrypt function just undoes the shifts.

key1 = 'messy'
key2 = 'yikes'
key3 = '2019'

# original message = 'There is an apple on the table. Do you want it?'
message = 'hlXD!0}"cfA&,xt|y#*pe`d7|k(s=<wKyq6%6_90=JZV_u+'

################################################################################

import random

d = ['|', 'A', 'z', '(', '2', 'O', '{', ')', '_', 'M', '6', 'k', 'U', 'I', 'j',
     '?', '8', '$', 'B', '`', '1', 'v', 'm', 'a', '^', 'R', 'f', 'g', 'b', 'L', 
     'o', 'H', 'l', '}', 'N', '[', '4', 'y', 'e', '5', 'u', '#', '*', 'Z', '/', 
     'x', 'P', '"', 'S', '~', '&', 'J', 'n', ']', 'Y', '@', '%', '-', 'G', '3', 
     '+', 'F', 'c', 's', ' ', '7', 't', 'w', 'i', '>', '<', 'C', 'X', 'E', 'W', 
     'q', 'V', 'T', 'h', 'r', 'K', '0', ',', '=', 'p', 'Q', '.', '!', ':', 'D', 
     'd', '9']

dor = {'|': 0, 'A': 1, 'z': 2, '(': 3, '2': 4, 'O': 5, '{': 6, ')': 7, '_': 8, 
       'M': 9, '6': 10, 'k': 11, 'U': 12, 'I': 13, 'j': 14, '?': 15, '8': 16, 
       '$': 17, 'B': 18, '`': 19, '1': 20, 'v': 21, 'm': 22, 'a': 23, '^': 24, 
       'R': 25, 'f': 26, 'g': 27, 'b': 28, 'L': 29, 'o': 30, 'H': 31, 'l': 32, 
       '}': 33, 'N': 34, '[': 35, '4': 36, 'y': 37, 'e': 38, '5': 39, 'u': 40, 
       '#': 41, '*': 42, 'Z': 43, '/': 44, 'x': 45, 'P': 46, '"': 47, 'S': 48, 
       '~': 49, '&': 50, 'J': 51, 'n': 52, ']': 53, 'Y': 54, '@': 55, '%': 56, 
       '-': 57, 'G': 58, '3': 59, '+': 60, 'F': 61, 'c': 62, 's': 63, ' ': 64, 
       '7': 65, 't': 66, 'w': 67, 'i': 68, '>': 69, '<': 70, 'C': 71, 'X': 72, 
       'E': 73, 'W': 74, 'q': 75, 'V': 76, 'T': 77, 'h': 78, 'r': 79, 'K': 80, 
       '0': 81, ',': 82, '=': 83, 'p': 84, 'Q': 85, '.': 86, '!': 87, ':': 88, 
       'D': 89, 'd': 90, '9': 91}


def dchr(t):
    return d[t % 92]


def dord(s):
    return dor[s]


def sh(s1, s2):
    s3 = s1 % s2
    if s3 < 1114111:
        return s3
    else:
        return sh(s2, s3)


def sw(sd):
    third_key = int(key3)
    key = int(''.join([str(ord(x)) for x in key1 + key2])) % 1031
    sw = []
    while len(sw) < len(message):
        random.seed(sd)
        se = random.randint(0, key)
        sw.append(se)
        sd = (se ** key) % third_key
    return sw


pub = int(''.join([str(ord(x)) for x in key1]))
pri = int(''.join([str(ord(x)) for x in key2]))

sh = sh(pub, pri)

sches = sw(sh)

encode_out = ''
decode_out = ''
for ind, cha in enumerate(message):
    encode_out += dchr(dord(cha) + sches[ind])
    decode_out += dchr(dord(cha) - sches[ind])

print('\nencode:\n' + encode_out)
print('\ndecode:\n' + decode_out + '\n')
