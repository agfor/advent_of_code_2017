#!/usr/bin/env pypy

from collections import defaultdict

grid = defaultdict(lambda: ".")
data = [line.strip() for line in open("input")]
for i, line in enumerate(data):
    for k, node in enumerate(line):
        grid[i, k] = node
x, y = 12, 12

direction = 0
infected = 0

for _ in range(10000000):
    if grid[x, y] == "#":
        direction = (direction + 1) % 4
        grid[x, y] = "F"
    elif grid[x, y] == ".":
        direction = (direction - 1) % 4
        grid[x, y] = "W"
    elif grid[x, y] == "F":
        direction = (direction + 2) % 4
        grid[x, y] = "."
    else:
        infected += 1
        grid[x, y] = "#"
    if direction == 0:
        x -= 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x += 1
    else:
        y -= 1
print(infected)
