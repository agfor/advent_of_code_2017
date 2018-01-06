#!/usr/bin/env pypy

from collections import defaultdict
from re import search

data = [line.rstrip() for line in open("input") if line.strip()]

current_state = data[0][-2]
debug_at = int(search(r"\d+", data[1]).group(0))
print(current_state, debug_at)

states = {}
for line in data[2:]:
    if line[0] == "I":
        new_state = states[line[9]] = {}
    elif line[2] == "I":
        value = int(line[-2])
        new_state[value] = {}
    elif line[6] == "W":
        new_state[value]["W"] = int(line[-2])
    elif line[6] == "M":
        if line[-3] == "f":
            new_state[value]["M"] = -1
        else:
            new_state[value]["M"] = 1
    elif line[6] == "C":
        new_state[value]["N"] = line[-2]
print(states)

tape = defaultdict(int)
cursor = 0

for i in range(debug_at):
    state = states[current_state]
    curr_val = tape[cursor]
    tape[cursor] = state[curr_val]["W"]
    cursor += state[curr_val]["M"]
    current_state = state[curr_val]["N"]

result = sum(tape.values())
print(result)
