#!/usr/bin/env python3

from itertools import count

data = [[int(x) for x in line.strip().split(": ")] for line in open("input")]
#data = [[0, 3], [1, 2], [4, 4], [6, 4]]

def calc(data, i):
    for layer, depth in data:
        length = (depth - 2) * 2 + 2
        if ((layer + i) % length) == 0:
            return False
    return True

for i in count():
    result = calc(data, i)
    if result:
        print(i)
        break
