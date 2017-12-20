#!/usr/bin/env pypy

maze = open("input").readlines()
x, y, x_dir, y_dir, char, seen = 0, 1, 1, 0, "|", []

while char != " ":
    seen.append(char)
    if char == "+":
        if x_dir:
            x_dir = 0
            y_dir = -1 if maze[x][y + 1] == " " else 1
        else:
            x_dir = -1 if maze[x + 1][y] == " " else 1
            y_dir = 0
    x, y = x + x_dir, y + y_dir
    char = maze[x][y]

print("".join(c for c in seen if c not in "-|+"))
print(len(seen))
