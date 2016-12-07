#!/usr/bin/env python3

import re

grid = [[0 for _ in range(1000)] for _ in range(1000)]

with open('six.in', 'r') as f:
    instructions = [l.strip() for l in f.readlines()]

for instr in instructions:
    m = re.match('(turn (on|off)|toggle) (\d+),(\d+) through (\d+),(\d+)', instr)
    if m.group(1) == 'toggle':
        arow, acol = map(int, m.group(3, 4))
        brow, bcol =map(int, m.group(5, 6))
        for row in range(arow, brow+1):
            for col in range(acol, bcol+1):
                grid[row][col] += 2
    elif m.group(2) == 'on':
        arow, acol = map(int, m.group(3, 4))
        brow, bcol = map(int, m.group(5, 6))

        for row in range(arow, brow+1):
            for col in range(acol, bcol+1):
                grid[row][col] += 1
    elif m.group(2) == 'off':
        arow, acol = map(int, m.group(3, 4))
        brow, bcol = map(int, m.group(5, 6))

        for row in range(arow, brow+1):
            for col in range(acol, bcol+1):
                if grid[row][col] > 0:
                    grid[row][col] -= 1

lumens = 0
for row in range(len(grid)):
    for col in range(len(grid)):
        lumens += grid[row][col]
print(lumens)
