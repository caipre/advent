#!/usr/bin/env python3

from enum import Enum

class Direction(Enum):
    north = 90
    east  = 0
    south = 270
    west  = 180

class Santa(object):
    def __init__(self, facing):
        self.x = 0
        self.y = 0
        self.facing = facing
        self.visited = set([(0, 0)])

    def turn(self, direction):
        angle = self.facing.value + (-90 if direction == 'R' else 90)
        self.facing = Direction(angle % 360)

    def move_forward(self, blocks):
        if   self.facing == Direction.north:
            return ((self.x, self.y + 1) for i in range(blocks))
        elif self.facing == Direction.east:
            return ((self.x + 1, self.y) for i in range(blocks))
        elif self.facing == Direction.south:
            return ((self.x, self.y - 1) for i in range(blocks))
        else:
            return ((self.x - 1, self.y) for i in range(blocks))

    def walk(self, blocks):
        for coord in self.move_forward(blocks):
            self.x, self.y = coord
            if coord in self.visited:
                return True
            self.visited.add(coord)

def taxicab_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

if __name__ == '__main__':
    santa = Santa(Direction.north)

    with open('one.in', 'r') as f:
        instructions = f.read().split(', ')

    for instr in instructions:
        direction, blocks = instr[0], int(instr[1:])
        santa.turn(direction)
        if santa.walk(blocks):
            break

    blocks = taxicab_distance((0, 0), (santa.x, santa.y))
    print('blocks to hq:', blocks)
