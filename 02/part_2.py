#!/usr/bin/env python3

from itertools import combinations

data = [[int(item) for item in line.split()] for line in open("input") if line]

sum = 0

for line in data:
    for combo in combinations(line, 2):
        quotient, remainder = divmod(*sorted(combo, reverse = True)) 
        if not remainder:
            sum += quotient

print(sum)
