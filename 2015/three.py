#!/usr/bin/env python3

with open('three.in', 'r') as f:
    directions = f.read()

class Sleigh(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.deliveries = set([(x, y)])

    def move(self, dir):
        if   dir == '^':
            self.y -= 1
        elif dir == '>':
            self.x += 1
        elif dir == 'v':
            self.y += 1
        elif dir == '<':
            self.x -= 1
        self.deliveries.add((self.x, self.y))


santa = Sleigh(0, 0)
robot = Sleigh(0, 0)

for i, dir in enumerate(directions):
    if i % 2:
        santa.move(dir)
    else:
        robot.move(dir)

print('santa deliveries:', len(santa.deliveries))
print('robot deliveries:', len(robot.deliveries))
print('total deliveries:', len(santa.deliveries | robot.deliveries))
