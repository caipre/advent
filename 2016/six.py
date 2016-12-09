#!/usr/bin/env python3

from collections import Counter

with open('six.in', 'r') as f:
    messages = [l.strip() for l in f.readlines()]

message = ''
for col in zip(*messages):
    chars = Counter(col)
    items = list(chars.items())
    items.sort(key=lambda i: i[1], reverse=True)
    message += items[-1][0]

print(message)
