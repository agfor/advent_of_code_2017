#!/usr/bin/env python3
source = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
data = [line.split(" -> ") for line in source.split("\n")]
data = [line.split(" -> ") for line in open("input")]

nodes = set()
children = set()

for line in data:
    nodes.add(line[0].split()[0].strip())
    if len(line) > 1:
        for item in line[1].split(", "):
            children.add(item.strip())
print(nodes)
print(children)
print(nodes - children)
