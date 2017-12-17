#!/usr/bin/env pypy

def main():
    num = 335
    index = 0
    target = None
    for i in range(1, 50000000 + 1):
        index = ((index + num) % i) + 1
        if index == 1:
            target = i
    print(target)

main()
