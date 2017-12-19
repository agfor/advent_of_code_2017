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

played = []
while 0 <= pos < len(new_ins):
    ins, first, second = new_ins[pos]
    if ins == "set":
        reg[first] = second if isinstance(second, int) else reg[second]
        pos += 1
    elif ins == "mul":
        reg[first] *= second if isinstance(second, int) else reg[second]
        pos += 1
    elif ins == "add":
        reg[first] += second if isinstance(second, int) else reg[second]
        pos += 1
    elif ins == "mod":
        reg[first] %= second if isinstance(second, int) else reg[second]
        pos += 1
    elif ins == "jgz":
        pos += (second if isinstance(second, int) else reg[second]) if (first if isinstance(first, int) else reg[first]) > 0 else 1
    elif ins == "snd":
        played.append(first if isinstance(first, int) else reg[first])
        pos += 1
    elif ins == "rcv":
        if reg[first] > 0:
            raise RuntimeError(str(played[-1]))
            #reg[first] = played[-1]
        pos += 1
    else:
        raise RuntimeError(ins)
