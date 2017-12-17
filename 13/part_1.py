#!/usr/bin/env python3

data = [[int(x) for x in line.strip().split(": ")] for line in open("input")]
#data = [[0, 3], [1, 2], [4, 4], [6, 4]]

total = 0
for layer, depth in data:
    length = (depth - 2) * 2 + 2
    if (layer % length) == 0:
        total += layer * depth

print(total)
