#!/usr/bin/env pypy

from collections import defaultdict

instructions = [line.strip().split() for line in open("input")]

reg = defaultdict(int)

new_ins = []
for line in instructions:
    ins = line[0]
    try:
        first = int(line[1])
    except:
        first = line[1]
    try:
        second = int(line[2])
    except:
        try:
            second = line[2]
        except:
            second = None
    new_ins.append((ins, first, second))

pos = 0
mul = 0
while 0 <= pos < len(new_ins):
    ins, first, second = new_ins[pos]
    if ins == "set":
        reg[first] = second if isinstance(second, int) else reg[second]
        pos += 1
    elif ins == "mul":
        reg[first] *= second if isinstance(second, int) else reg[second]
        mul += 1
        pos += 1
    elif ins == "sub":
        reg[first] -= second if isinstance(second, int) else reg[second]
        pos += 1
    elif ins == "jnz":
        if (first if isinstance(first, int) else reg[first]) != 0:
            pos += (second if isinstance(second, int) else reg[second])
        else:
            pos += 1

print(mul)
