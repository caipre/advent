#!/usr/bin/env python3

with open('four.in', 'r') as f:
    rooms = (line.strip() for line in f.readlines())

def is_valid_room(room):
    cs = {}
    for c in room:
        if c == '-': continue
        if c.isdigit(): break
        try: cs[c] += 1
        except: cs[c] = 1

    items = list(cs.items())
    items.sort(key=lambda it: it[0]) # character
    items.sort(key=lambda it: it[1], reverse=True) # frequency
    checkkey = ''.join(it[0] for it in items[:5])

    return checkkey == room[-6:-1]

def sector(room):
    i = room.rindex('-') + 1
    j = room.index('[', i)
    return int(room[i:j])

def rotated(room, sector):
    s = ''
    sector %= 26
    for c in room:
        if c == '-':
            s += ' '
            continue
        if c.isdigit():
            break
        s += chr(0x61 + (((ord(c) - 0x61) + sector) % 26))
    return s

sumsector = 0
decrypted = []
for room in rooms:
    if not is_valid_room(room):
        continue
    s = sector(room)
    sumsector += s
    decrypted.append((rotated(room, s), room))

print('sum vaild sectors:', sumsector)
print('decrypted rooms:')
for name, room in decrypted:
    print(name, room)
