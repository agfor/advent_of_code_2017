#!/usr/bin/env pypy

from collections import defaultdict

data = [tuple(map(int, line.strip().split("/"))) for line in open("input") if line.strip()]

comps = defaultdict(list)

for line in data:
    comps[line[0]].append(line)
    if line[0] != line[1]:
        comps[line[1]].append(line)

def max_path(start, data, path):
    score = 0
    for comp in comps[start]:
        if comp not in path:
            end = comp[0] if comp[1] == start else comp[1]
            new_path = path.union([comp])
            new_score = sum(comp) + max_path(end, data, new_path)
            if new_score > score:
                score = new_score
    return score

result = max_path(0, data, set())
print(result)
