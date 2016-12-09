#!/usr/bin/env python3

import re

def rect(m, screen):
    a, b = map(int, m.groups())
    for row in range(b):
        for col in range(a):
            screen[row][col] = True

def rotate(m, screen):
    width = len(screen[0])
    height = len(screen)

    what, which, by = m.group(1), *map(int, m.group(2, 3))
    if   what == 'row':
        screen[which] = [screen[which][(i-by)%width] for i in range(width)]
    elif what == 'column':
        col = [screen[row][which] for row in range(height)]
        for row in range(height):
            screen[(row+by)%height][which] = col[row]

screen = [[False for _ in range(50)] for _ in range(6)]

patterns = [
    (rect, r'rect (\d+)x(\d+)'),
    (rotate, r'rotate (row|column) [xy]=(\d+) by (\d+)'),
]

with open('eight.in', 'r') as f:
    instructions = [l.strip() for l in f.readlines()]

for instr in instructions:
    for fn, patt in patterns:
        m = re.match(patt, instr)
        if m: fn(m, screen)


n = 0
for row in range(len(screen)):
    for col in range(len(screen[0])):
        if screen[row][col]: n += 1
        print('#' if screen[row][col] else '.', end='')
    print()
print(n)
