#!/usr/bin/env python3

import hashlib

puzzle = b'abbhdwsy'

bytes_for = lambda i: i.to_bytes((i.bit_length() // 8) + 1, byteorder='big')
bytes_for = lambda i: bytes(str(i), 'ascii')

i = 0
g = 0
password = [None] * 8
while g < 8:
    h = hashlib.md5(puzzle + bytes_for(i)).hexdigest()
    i += 1
    if h.startswith('00000'):
        print(h, password, i)
        t = int(h[5], 16)
        if t >= len(password):
            continue
        if password[t] is not None:
            continue
        password[t] = h[6]
        g += 1

print(''.join(password))
