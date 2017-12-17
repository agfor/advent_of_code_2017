#!/usr/bin/env python3

"hxtvlmkl"


from itertools import count
from operator import xor
from functools import reduce

SIZE = 256
ROUNDS = 64
lengths = [ord(i) for i in open("input").read().strip()]
#lengths = [ord(i) for i in "1,2,4"]
grid = []
for j in range(128):
    lengths = [ord(i) for i in "hxtvlmkl-" +str(j)]

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
    result = "".join(hashes)

    grid.append(bin(int(result,16))[2:].zfill(128))
print("\n".join(grid))

points = {(x, y): None for x in range(128) for y in range(128) if grid[x][y] == "1"}

def update(x, y, region):
    if (x, y) not in points or points[x, y] is not None:
        return False
    points[x, y] = region
    for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        update(*neighbor, region)
    return True

region = 0
for point in points:
    if update(*point, region):
        region += 1

print(region)
