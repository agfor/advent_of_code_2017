#!/usr/bin/env python3

data = open("input").read()
#data = "s1,x3/4,pe/b\\n"
data = data.strip().split(",")

dancers = list("abcdefghijklmnop")
#dancers = list("abcde")

for move in data:
    if move[0] == "x":
        first, second = [int(x) for x in move[1:].split("/")]
        dancers[first], dancers[second] = dancers[second], dancers[first]
    elif move[0] == "p":
        first, second = [dancers.index(x) for x in move[1:].split("/")]
        dancers[first], dancers[second] = dancers[second], dancers[first]
    else:
        spin = int(move[1:])
        dancers = dancers[-spin:] + dancers[:-spin]

print("".join(dancers))
