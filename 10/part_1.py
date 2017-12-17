#!/usr/bin/env python3

SIZE = 256
lengths = [int(i) for i in open("input").read().split(",")]

#SIZE = 5
#lengths = 3, 4, 1, 5

index = 0
skips = range(len(lengths))
data = list(range(SIZE))

for length, skip in zip(lengths, skips):
    if index + length > SIZE - 1:
        extra = (index + length) % SIZE
        piece = list(reversed(data[index:] + data[:extra]))
        data[index:] = piece[:len(data) - index]
        data[:extra] = piece[len(data) - index:]
    else:
        piece = list(reversed(data[index:index + length]))
        data[index:index + length] = piece
    index = (index + length + skip) % SIZE

print(data[0] * data[1])
