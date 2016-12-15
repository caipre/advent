#!/usr/bin/env python3

from copy import deepcopy
import re

discs = []

with open('fifteen.in', 'r') as f:
    for line in f:
        m = re.match(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', line)
        disc, npositions, position = map(int, m.group(1, 2, 3))
        discs.append((npositions, position))

    discs.append((11, 0))

presstime = 0
fallthrough = False
while not fallthrough:
    t = presstime + 1
    for i, (mod, pos) in enumerate(discs):
        #print('t', (t + i), 'disc', i, 'is at pos', pos + (t + i), '->', (pos + (t + i)) % mod, 'with mod', mod)
        if (pos + (t + i)) % mod != 0:
            presstime += 1
            break
    else:
        fallthrough = True

print(presstime)
