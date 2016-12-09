#!/usr/bin/env python3

import re

def is_abba(s):
    return any(s[i:i+2] == s[i+2:i+4][::-1] for i in range(len(s)-3) if s[i] != s[i+1])

def is_tls(ipv7):
    hypernet = re.compile(r'\[[a-z]+\]')
    if any(map(is_abba, hypernet.findall(ipv7))): return False
    return any(map(is_abba, hypernet.split(ipv7)))

def aba(s):
    return (s[i:i+3] for i in range(len(s)-2) if s[i] == s[i+2] != s[i+1])

def to_bab(s):
    return (s+s[1:])[1:4]

def is_ssl(ipv7):
    hypernet = re.compile(r'\[[a-z]+\]')
    hyperabas = set(a for s in hypernet.findall(ipv7) for a in aba(s))
    superabas = set(a for s in hypernet.split(ipv7) for a in aba(s))
    return any(bab in superabas for bab in map(to_bab, hyperabas))

with open('seven.in', 'r') as f:
    print(list(map(is_ssl, f)).count(True))
