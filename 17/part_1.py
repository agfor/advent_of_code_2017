#!/usr/bin/env pypy

num = 335
buffer = [0]
index = 0
for i in range(1, 2017 + 1):
    index = ((index + num) % len(buffer)) + 1
    buffer.insert(index, i)

print(buffer[(index + 1) % len(buffer)])
