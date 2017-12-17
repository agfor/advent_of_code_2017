#!/usr/bin/env python3

data = list(open("input").read())

in_garbage = False
next_canceled = False
count = 0
score = 0
next_score = 1

for char in data:
    if in_garbage:
        if next_canceled:
            next_canceled = False
        elif char == "!":
            next_canceled = True
        elif char == ">":
            in_garbage = False
        else:
            count += 1
    else:
        if char == "{":
            score += next_score
            next_score += 1
        elif char == "}":
            next_score -= 1
        elif char == "<":
            in_garbage = True

print(count)
print(score)
