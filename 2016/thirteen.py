#!/usr/bin/env python3

from collections import namedtuple
from collections import deque
from copy import copy

Coord = namedtuple('Coord', ['x', 'y'])

def neighbors(coord):
    if coord.y > 0: yield Coord(coord.x, coord.y - 1) # north
    yield Coord(coord.x + 1, coord.y) # east
    yield Coord(coord.x, coord.y + 1) # south
    if coord.x > 0: yield Coord(coord.x - 1, coord.y) # west

def is_wall(coord):
    puzzle = 1350
    x, y = coord.x, coord.y
    equ = x*x + 3*x + 2*x*y + y + y*y
    equ += puzzle
    return bin(equ).count('1') % 2 != 0

def bfs(start, target):
    seen = set()
    q = deque([(start, [])])
    while q:
        coord, path = q.popleft()
        #if coord == target:
        #    print(path)
        #    print(len(path))
        #    break
        if len(path) == 50:
            continue
        for n in neighbors(coord):
            if n in seen:
                continue
            if is_wall(n):
                continue
            seen.add(n)
            q.append((n, path + [n]))
    print(len(seen))

start = Coord(x=1, y=1)
target = Coord(x=31, y=39)
bfs(start, target)
