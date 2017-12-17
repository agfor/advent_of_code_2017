#!/usr/bin/env python3

from itertools import count

data = [int(line) for line in open("input")]
offset = 0

try:
    for i in count(0):
        new_offset = offset + data[offset]
        data[offset] += 1
        offset = new_offset
except IndexError:
    print(i)
