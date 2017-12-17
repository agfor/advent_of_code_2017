#!/usr/bin/env python3

from itertools import count

data = [int(x) for x in open("input").read().split()]
#data = [0, 2, 7, 0] 

seen = set()

for num in count():
    if tuple(data) in seen:
        break
    else:
        seen.add(tuple(data))
    high = index = 0
    for i, item in enumerate(data):
        if item > high:
            index, high = i, item

    data[index] = 0
    for i in range(1, high + 1):
        data[(index + i) % len(data)] += 1 

print(num)
