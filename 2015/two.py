#!/usr/bin/env python3

def paper(l, w, h):
    m = min((l*w), (w*h), (h*l))
    return 2*((l*w) + (w*h) + (h*l)) + m

def ribbon(l, w, h):
    bow = l * w * h
    ss = [l, w, h]
    ss.sort()
    return bow + 2*(ss[0] + ss[1])

with open('two.in', 'r') as f:
    dimensions = f.readlines()

total = {'paper': 0, 'ribbon': 0}
for dim in dimensions:
    l, w, h = map(int, dim.split('x'))
    total['paper'] += paper(l, w, h)
    total['ribbon'] += ribbon(l, w, h)

print('totals:', total)
