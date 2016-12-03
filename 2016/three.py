#!/usr/bin/env python3

with open('three.in', 'r') as f:
    tris = [line.split() for line in f.readlines()]

def is_valid(tri):
    a, b, c = map(int, tri)
    return a + b > c and a + c > b and b + c > a

nvalid = sum(1 for tri in tris if is_valid(tri))
print('valid triangles:', nvalid)

nvalidcols = sum(1 for col in zip(*tris)
                   for tri in zip(*[iter(col)]*3) if is_valid(tri))
print('valid columnar triangles:', nvalidcols)
