#!/usr/bin/env python3

data = [line.split() for line in open("input")]
print(sum(1 for line in data if len(line) == len(set(line))))
