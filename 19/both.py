#!/usr/bin/env pypy

maze = open("input").readlines()

x, y = 0, 1
x_dir, y_dir = 1, 0

seen = []
steps = 0

while maze[x][y] != " ":
    steps += 1
    char = maze[x][y]
    if char not in "-|+":
        seen.append(char)
    if char == "+":
        if y_dir == 0:
            x_dir = 0
            if maze[x][y + 1] != " ":
                y_dir = 1
            else:
                y_dir = -1
            y += y_dir
        else:
            y_dir = 0
            if maze[x + 1][y] != " ":
                x_dir = 1
            else:
                x_dir = -1
            x += x_dir
    elif y_dir == 0:
        x += x_dir
    elif x_dir == 0:
        y += y_dir
    else:
        raise

print("".join(seen))
print(steps)
