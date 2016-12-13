#!/usr/bin/env python3

from collections import deque
from collections import namedtuple

import re

robots = {}
outputs = {}

with open('ten.in', 'r') as f:
    for line in f:
        m = re.match(r'value (\d+) goes to bot (\d+)', line)
        if m:
            value, bot = map(int, m.groups())
            try:
                robots[bot]['values'].append(value)
            except:
                robots[bot] = {'values': [value]}
            continue

        m = re.match(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line)
        if m:
            low_to, high_to = m.group(2, 4)
            bot, low_id, high_id = map(int, m.group(1, 3, 5))
            if bot not in robots:
                robots[bot] = {'values': []}
            robots[bot]['low'] = (low_to, low_id)
            robots[bot]['high'] = (high_to, high_id)
            continue

        assert False

completed = set()
workq = deque(botid for botid in robots if len(robots[botid]['values']) == 2)
while workq:
    botid = workq.popleft()

    if botid in completed: continue

    robots[botid]['values'].sort()
    low, high = robots[botid]['values']

    print('{:3d}'.format(botid), robots[botid])

    if low == 17 and high == 61:
        print('special bot:', botid)

    for z in ('low', 'high'):
        val = low if z == 'low' else high
        to, id = robots[botid][z]
        if to == 'bot':
            robots[id]['values'].append(val)
            assert len(robots[id]['values']) <= 2
        elif to == 'output':
            assert id not in outputs
            outputs[id] = val

    completed.add(botid)

    for id in robots:
        if len(robots[id]['values']) == 2:
            workq.append(id)

print(outputs)
print(outputs[0], outputs[1], outputs[2])
