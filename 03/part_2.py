#!/usr/bin/env python3

from itertools import cycle, product, count, chain

def index_generator(x = 0, y = 0):
    repeats = chain.from_iterable(zip(count(1), count(1)))
    directions = cycle(((1, 0), (0, 1), (-1, 0), (0, -1)))
    for (dx, dy), repeat in zip(directions, repeats):
        for _ in range(repeat):
            x += dx
            y += dy
            yield x, y

def neighborhood(x, y):
    return ((x + dx, y + dy) for dx, dy in product((-1, 0, 1), repeat = 2))

data = {(0, 0): 1}

for x, y in index_generator():
    result = data[x, y] = sum(data.get((i, j), 0) for i, j in neighborhood(x, y))
    if result > 368078:
        print(result)
        break
