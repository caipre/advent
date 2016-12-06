#!/usr/bin/env python3

pos = None
floor = 0

with open('one.in', 'r') as f:
    instructions = f.read()

for i, c in enumerate(instructions):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
        if pos is None and floor == -1:
            pos = i + 1

print('final floor:', floor)
print('enter basement:', pos)
