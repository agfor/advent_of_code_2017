#!/usr/bin/env python3

from collections import defaultdict

instructions = [line.split() for line in open("input")]
#instructions = map(str.split, """b inc 5 if a > 1
#a inc 1 if b < 5
#c dec -10 if a >= 1
#c inc -20 if c == 10""".split("\n"))

localstate = defaultdict(int)
maxval = 0
for reg, ins, amount, _, other_reg, comp, val in instructions:
    code = "if {} {} {}: {} {} {}".format(other_reg, comp, val, reg, ("+=" if ins == "inc" else "-="), amount)
    exec(code, {}, localstate)
    maxval = max(max(localstate.values()), maxval)

print(max(localstate.values()))
print(maxval)
