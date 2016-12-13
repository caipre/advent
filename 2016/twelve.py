#!/usr/bin/env python3

import re

registers = {c: 0 for c in ('a', 'b', 'c', 'd')}
registers['c'] = 1

def cpy(rs, iptr, src, dst):
    rs[dst] = int(src) if src.isdigit() else rs[src]
    return iptr + 1

def inc(rs, iptr, reg):
    rs[reg] += 1
    return iptr + 1

def dec(rs, iptr, reg):
    rs[reg] -= 1
    return iptr + 1

def jnz(rs, iptr, reg, offset):
    if reg.isdigit() and int(reg) != 0:
        return iptr + int(offset)
    if rs[reg] != 0:
        return iptr + int(offset)
    return iptr + 1

patterns = (
    (cpy, r'cpy (\w+) (\w+)'),
    (inc, r'inc (\w+)'),
    (dec, r'dec (\w+)'),
    (jnz, r'jnz (-?\w+) (-?\w+)'),
)

with open('twelve.in', 'r') as f:
    instructions = [l.strip() for l in f.readlines()]

iptr = 0
while iptr < len(instructions):
    instr = instructions[iptr]
    #print(instr, registers)
    for fn, patt in patterns:
        m = re.match(patt, instr)
        if not m: continue
        iptr = fn(registers, iptr, *m.groups())

print(registers)
