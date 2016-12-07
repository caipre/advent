#!/usr/bin/env python3

import re

with open('five.in', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

def personality(line):
    if any(s in line for s in ('ab', 'cd', 'pq', 'xy')):
        return False
    vowels = 'aeiou'
    prev = line[0]
    ds = False
    vs = 1 if prev in vowels else 0
    for i in range(1,len(line)):
        c = line[i]
        if c in vowels: vs += 1
        if prev == c: ds = True
        prev = c
    return vs >= 3 and ds

print(len([l for l in lines if personality(l)]))

def temperament(line):
    return (re.search(r'(..).*?\1', line) and re.search(r'(.)(.)\1', line)) is not None

print(len([l for l in lines if temperament(l)]))
