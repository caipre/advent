#!/usr/bin/env python3

from collections import deque
from functools import reduce

import operator
import re

class CircuitBoard(object):
    def __init__(self):
        self.evalq = deque()
        self.wires = {}
        self.conns = {}

    def add(self, gate):
        assert gate.outw not in self.wires
        self.wires[gate.outw] = None

        if gate.is_settled():
            self.evalq.append(gate)

        for wire in gate.needs:
            try: self.conns[wire].add(gate)
            except: self.conns[wire] = set([gate])

    def eval(self):
        while self.evalq:
            gate = self.evalq.popleft()
            outw = gate.outw
            self.wires[outw] = gate.eval()

            if outw not in self.conns:
                continue

            for dep in self.conns[outw]:
                dep.settle(outw, self.wires[outw])
                if dep.is_settled():
                    self.evalq.append(dep)

class Gate(object):
    maxint = 0xffff

    def __init__(self, m):
        self.inputs = []
        self.needs = set()
        for g in m.groups()[:-1]:
            if g.isdigit():
                self.inputs.append(int(g))
            else:
                self.inputs.append(g)
                self.needs.add(g)
        self.outw = m.group('outw')

    def settle(self, wire, val):
        i = self.inputs.index(wire)
        self.inputs[i] = val
        self.needs.remove(wire)

    def is_settled(self):
        return len(self.needs) == 0

class SignalGate(Gate):
    def __init__(self, m):
        super(SignalGate, self).__init__(m)

    def eval(self):
        return self.inputs[0]

class AndGate(Gate):
    def __init__(self, m):
        super(AndGate, self).__init__(m)

    def eval(self):
        return reduce(operator.and_, self.inputs)

class OrGate(Gate):
    def __init__(self, m):
        super(OrGate, self).__init__(m)

    def eval(self):
        return reduce(operator.or_, self.inputs)

class NotGate(Gate):
    def __init__(self, m):
        super(NotGate, self).__init__(m)

    def eval(self):
        return (~self.inputs[0]) & self.maxint

class LShiftGate(Gate):
    def __init__(self, m):
        super(LShiftGate, self).__init__(m)

    def eval(self):
        return (self.inputs[0] << self.inputs[1]) & self.maxint

class RShiftGate(Gate):
    def __init__(self, m):
        super(RShiftGate, self).__init__(m)

    def eval(self):
        return (self.inputs[0] >> self.inputs[1]) & self.maxint

with open('seven.in', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

patterns = (
    (SignalGate, '^(\w+) -> (?P<outw>\w+)$'),
    (NotGate, '^NOT (\w+) -> (?P<outw>\w+)$'),
    (AndGate, '^(\w+) AND (\w+) -> (?P<outw>\w+)$'),
    (OrGate, '^(\w+) OR (\w+) -> (?P<outw>\w+)$'),
    (LShiftGate, '^(\w+) LSHIFT (\w+) -> (?P<outw>\w+)$'),
    (RShiftGate, '^(\w+) RSHIFT (\w+) -> (?P<outw>\w+)$'),
)

board = CircuitBoard()
for line in lines:
    for gate, regexp in patterns:
        m = re.match(regexp, line)
        if not m: continue
        board.add(gate(m))
        break

board.eval()
for k, v in sorted(board.wires.items(), key=lambda kv: kv[0]):
    print('{}: {}'.format(k, v))
