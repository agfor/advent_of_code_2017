#!/usr/bin/env python3

from itertools import count

data = [int(x) for x in open("input").read().split()]
#data = [0, 2, 7, 0]

seen = set()

while not tuple(data) in seen:
    seen.add(tuple(data))
    high = index = 0
    for i, item in enumerate(data):
        if item > high:
            index, high = i, item

    data[index] = 0
    quotient, remainder = divmod(high, len(data))
    data = [item + quotient for item in data]
    for i in range(1, remainder + 1):
        data[(index + i) % len(data)] += 1

print(len(seen))
