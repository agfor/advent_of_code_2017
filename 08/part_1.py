#!/usr/bin/env python3

from collections import defaultdict

instructions = [line.split() for line in open("input")]
#instructions = map(str.split, """b inc 5 if a > 1
#a inc 1 if b < 5
#c dec -10 if a >= 1
#c inc -20 if c == 10""".split("\\n"))

data = defaultdict(int)


maxval = 0
for reg, ins, amount, _, other_reg, comp, val in instructions:
    comp = {"<": "__lt__", ">": "__gt__", ">=": "__ge__", "<=": "__le__", "==": "__eq__", "!=": "__ne__"}[comp]
    if getattr(int, comp)(data[other_reg], int(val)):
        if ins == "inc":
            result = data[reg] = data[reg] + int(amount)
        else:
            result = data[reg] = data[reg] - int(amount)
        if result > maxval:
            maxval = result

print(max(data.values()))
print(maxval)
