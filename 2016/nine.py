#!/usr/bin/env python3

import re
from collections import deque

def decompress(s):
    ret = ''
    compressed = deque(s)
    while compressed:
        c = compressed.popleft()
        if c != '(':
            ret += c
        else:
            nchars = ''
            while True:
                c = compressed.popleft()
                if c == 'x': break
                nchars += c
            nchars = int(nchars)

            nreps = ''
            while True:
                c = compressed.popleft()
                if c == ')': break
                nreps += c
            nreps = int(nreps)

            repstr = ''.join([compressed.popleft() for _ in range(nchars)])
            ret += repstr * nreps
    return ret

def declen(s):
    ret = 0
    compressed = deque(s)
    while compressed:
        c = compressed.popleft()
        if c != '(':
            ret += 1
        else:
            nchars = ''
            while True:
                c = compressed.popleft()
                if c == 'x': break
                nchars += c
            nchars = int(nchars)

            nreps = ''
            while True:
                c = compressed.popleft()
                if c == ')': break
                nreps += c
            nreps = int(nreps)

            repstr = ''.join([compressed.popleft() for _ in range(nchars)])
            ret += declen(repstr) * nreps
    return ret
            
assert decompress('ADVENT') == 'ADVENT'
assert decompress('A(1x5)BC') == 'ABBBBBC'
assert decompress('(3x3)XYZ') == 'XYZXYZXYZ'
assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
assert decompress('(6x1)(1x3)A') == '(1x3)A'
assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'
            
with open('nine.in', 'r') as f:
    data = f.read().strip()
    print(len(decompress(data)))
    print(declen(data))
