#!/usr/bin/env pypy

def dist(args):
    return sum(map(abs, args))

data = open("input").readlines()
accs = [line.split("<")[-1] for line in data]
accs = [[int(x) for x in line[:-2].split(",")] for line in accs]
print(min(enumerate(accs), key = lambda (i, acc): dist(acc)))
