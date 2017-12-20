#!/usr/bin/env pypy

from itertools import count
from json import loads
from collections import defaultdict

data = open("input").read()
data = "{" + data.strip().replace("=", ":").replace("<", "[").replace(">", "]").replace("\n", "}\n{").replace("p", '"p"').replace("v", '"v"').replace("a", '"a"') + "}"
data = [loads(line) for line in data.split("\n")]
data = [{k: tuple(v) for k, v in line.items()} for line in data]

def tup_sum(*args):
    return tuple(sum(xs) for xs in zip(*args))

last_col = -1

for time in count():
    if time - last_col > 1000:
        break
    coords = defaultdict(list)
    for line in data:
        coords[line["p"]].append(line)
        line["v"] = tup_sum(line["v"], line["a"])
        line["p"] = tup_sum(line["v"], line["p"])
    new_data = []
    for _, lines in coords.items():
        if len(lines) == 1:
            new_data.append(lines[0])
        else:
            last_col = time
    data = new_data
print(len(data))
print(last_col)
