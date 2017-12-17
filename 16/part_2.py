#!/usr/bin/env python3

def dance(dancers, moves):
    for move, first, second in moves:
        if move == "x":
            dancers[first], dancers[second] = dancers[second], dancers[first]
        elif move == "p":
            first, second = dancers.index(first), dancers.index(second)
            dancers[first], dancers[second] = dancers[second], dancers[first]
        else:
            dancers = dancers[first:] + dancers[:first]

def main():
    data = open("input").read()
    #data = "s1,x3/4,pe/b\\n"
    data = data.strip().split(",")

    dancers = list("abcdefghijklmnop")
    #dancers = list("abcde")

    moves = []
    for move in data:
        if move[0] == "x":
            first, second = [int(x) for x in move[1:].split("/")]
            move = ("x", first, second)
        elif move[0] == "p":
            first, second = move[1:].split("/")
            move = ("p", first, second)
        else:
            spin = int(move[1:])
            move = ("s", -spin, None)
        moves.append(move)

    seen = set()
    dance_string = "".join(dancers)
    while dance_string not in seen:
        dance(dancers, moves)
        dance_string = "".join(dancers)
        seen.add(dance_string)

    dancers = list("abcdefghijklmnop")

    for i in range(1000000000 % len(seen)):
        dance(dancers, moves)

    return dancers

print("".join(main()))
