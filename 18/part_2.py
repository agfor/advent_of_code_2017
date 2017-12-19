#!/usr/bin/env pypy

from collections import defaultdict, deque

inp = open("input")
instructions = [line.strip().split() for line in inp]

reg_0 = defaultdict(int)
reg_1 = defaultdict(int)
reg_1["p"] += 1

new_ins = []
for line in instructions:
    ins = line[0]
    try:
        first = int(line[1])
    except:
        first = line[1]
    try:
        second = int(line[2])
    except:
        try:
            second = line[2]
        except:
            second = None
    new_ins.append((ins, first, second))

state_0 = {"zero": True, "pos": 0, "reg": reg_0, "own": deque(), "other": deque(), "sends": 0}
state_1 = {"zero": False, "pos": 0, "reg": reg_1, "own": state_0["other"], "other": state_0["own"], "sends": 0}
state = state_0

while 0 <= state["pos"] < len(new_ins):
    ins, first, second = new_ins[state["pos"]]
    if ins == "set":
        state["reg"][first] = second if isinstance(second, int) else state["reg"][second]
        state["pos"] += 1
    elif ins == "mul":
        state["reg"][first] *= second if isinstance(second, int) else state["reg"][second]
        state["pos"] += 1
    elif ins == "add":
        state["reg"][first] += second if isinstance(second, int) else state["reg"][second]
        state["pos"] += 1
    elif ins == "mod":
        state["reg"][first] %= second if isinstance(second, int) else state["reg"][second]
        state["pos"] += 1
    elif ins == "jgz":
        if (first if isinstance(first, int) else state["reg"][first]) > 0:
            state["pos"] += (second if isinstance(second, int) else state["reg"][second])
        else:
            state["pos"] += 1
    elif ins == "snd":
        state["sends"] += 1
        state["other"].appendleft(first if isinstance(first, int) else state["reg"][first])
        state["pos"] += 1
    elif ins == "rcv":
        if state["own"]:
            state["reg"][first] = state["own"].pop()
            state["pos"] += 1
        else:
            if state["other"]:
                if state["zero"]:
                    state = state_1
                else:
                    state = state_0
            else:
                break
    else:
        raise RuntimeError(ins)
print(state_1["sends"])
