#!/usr/bin/env python3

import hashlib

puzzle = b'ckczppom'

i = 0
while True:
    h = hashlib.md5(puzzle + bytes_for(i)).hexdigest()
    if h.startswith('000000'):
        break
    i += 1

print(i)
