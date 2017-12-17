#!/usr/bin/env python3

data = [[int(item) for item in line.split()] for line in open("input") if line]

result = sum(max(line) - min(line) for line in data)

print(result)
