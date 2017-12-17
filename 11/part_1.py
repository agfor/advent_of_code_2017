#!/usr/bin/env python3
from collections import Counter

data = open("input").read().strip().split(",")
#data = "se,sw,se,sw,sw".split(",")

moves = Counter(data)

dirs = {
    ("n", "se"): "ne",
    ("n", "s"): None,
    ("n", "sw"): "nw",
    ("ne", "s"): "se",
    ("ne", "sw"): None,
    ("ne", "nw"): "n",
    ("nw", "se"): None,
    ("nw", "s"): "sw",
    ("se", "sw"): "s",
}

changed = True
while changed:
    changed = False
    for (first, second), replacement in dirs.items():
        if moves[first] and moves[second]:
            changed = True
            moves[first] -= 1
            moves[second] -= 1
            if replacement:
                moves[replacement] += 1

print(sum(moves.values()))
