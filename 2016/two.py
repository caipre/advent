#!/usr/bin/env python3

def standard(instructions, key=5):
    code = ''
    for line in instructions:
        for instr in line:
            if   instr == 'U' and key > 3:
                key -= 3
            elif instr == 'D' and key < 6:
                key += 3
            elif instr == 'L' and key % 3 != 1:
                key -= 1
            elif instr == 'R' and key % 3 != 0:
                key += 1
        code += str(key)
    return code

def diamond(instructions, key=5):
    keypad = '.0010002340567890ABC000D00'
    code = ''
    for line in instructions:
        for instr in line:
            if   instr == 'U' and keypad[key] not in ('1', '2', '4', '5', '9'):
                key -= 5
            elif instr == 'D' and keypad[key] not in ('5', '9', 'A', 'C', 'D'):
                key += 5
            elif instr == 'L' and keypad[key] not in ('1', '2', '5', 'A', 'D'):
                key -= 1
            elif instr == 'R' and keypad[key] not in ('1', '4', '9', 'C', 'D'):
                key += 1
        assert keypad[key] != '0'
        code += keypad[key]
    return code

if __name__ == '__main__':
    with open('two.in', 'r') as f:
        lines = f.readlines()

    print('standard:', standard(lines))
    print('diamond:', diamond(lines))
