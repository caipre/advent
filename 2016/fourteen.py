#!/usr/bin/env python3

import hashlib

salt = b'qzyelonm'

keys = []
n = -1
hashes = {}
while len(keys) < 64:
    n += 1
    h0 = hashlib.md5(salt + str(n).encode()).hexdigest()
    if h0 in hashes:
        h0 = hashes[h0]
    else:
        h0_ = h0
        for _ in range(2016):
            h0 = hashlib.md5(h0.encode()).hexdigest()
        hashes[h0_] = h0

    for i in range(2,len(h0)):
        if h0[i] == h0[i-1] == h0[i-2]:
            c = h0[i]
            break
    else:
        continue

    for i in range(n+1, n+1001):
        h = hashlib.md5(salt + str(i).encode()).hexdigest()
        if h in hashes:
            h = hashes[h]
        else:
            h_ = h
            for _ in range(2016):
                h = hashlib.md5(h.encode()).hexdigest()
            hashes[h_] = h
        if c * 5 in h:
            print('{:5d} {:5d} {} {} {}'.format(n, i, c, h0, h))
            keys.append(h0)
            break

print(n, len(keys))
