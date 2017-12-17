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
#data = [line.split(" -> ") for line in source.split("\\n")]
data = [line.split(" -> ") for line in open("input")]


dataset = {}

for line in data:
    key, weight = line[0].split()
    item = dataset[key] = {"weight": int(weight[1:-1])}

    if len(line) > 1:
        item["children"] = [item.strip() for item in line[1].split(", ")]

def calc_weights(dataset, key):
    item = dataset[key]
    if "total_weight" not in item:
        item["total_weight"] = item["weight"]
        if "children" in item:
            item["total_weight"] += sum(calc_weights(dataset, k) for k in item["children"])
    return item["total_weight"]

for key in dataset:
    calc_weights(dataset, key)

for key in dataset:
    item = dataset[key]
    if "children" in item:
        weights = [dataset[child]["total_weight"] for child in item["children"]]
        if len(set(weights)) > 1:
            print(weights)
            print(item["children"])
            break

print(dataset["tlskukk"]["weight"])
