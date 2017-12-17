#!/usr/bin/env python3

from itertools import count

#data = [int(x) for x in open("input").read().split()]
data = [0, 2, 7, 0]

seen = {}

for num in count():
    item = tuple(data)
    if item in seen:
        print(len(seen))
        print(len(seen) - seen[item])
        break
    else:
        seen[item] = num

    high = index = 0
    for i, item in enumerate(data):
        if item > high:
            index, high = i, item

    data[index] = 0
    quotient, remainder = divmod(high, len(data))
    data = [item + quotient + (1 if ((i - 1 - index) % len(data)) < remainder else 0)
                for i, item in enumerate(data)]
