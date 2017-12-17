#!/usr/bin/env python3
from collections import Counter

data = open("input").read().strip().split(",")

def dist(moves):
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
    for (first, second), replacement in dirs.items():
        if moves[first] and moves[second]:
            moves[first] -= 1
            moves[second] -= 1
            if replacement:
                moves[replacement] += 1
            break
    return sum(moves.values())        

last = highest = 0
moves = Counter()
for move in data:
    moves[move] += 1 
    last = dist(moves)
    highest = max(last, highest)

print(last, highest)
