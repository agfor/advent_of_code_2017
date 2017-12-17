#!/usr/bin/env python3

from itertools import count
from operator import xor
from functools import reduce

SIZE = 256
ROUNDS = 64
lengths = [ord(i) for i in open("input").read().strip()]
#lengths = [ord(i) for i in "1,2,4"]

lengths += [17,31,73,47,23]
index = 0
data = list(range(SIZE))
skips = count()

for _ in range(ROUNDS):
    for length, skip in zip(lengths, skips):
        if index + length >= SIZE:
            extra = (index + length) % SIZE
            piece = list(reversed(data[index:] + data[:extra]))
            data[index:] = piece[:len(data) - index]
            data[:extra] = piece[len(data) - index:]
        else:
            piece = list(reversed(data[index:index + length]))
            data[index:index + length] = piece
        index = (index + length + skip) % SIZE

hashes = ["{0:02x}".format(reduce(xor, data[i * 16:(i + 1) * 16]))
            for i in range(16)]
print("".join(hashes))
