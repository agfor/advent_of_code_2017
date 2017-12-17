#!/usr/bin/env python3

def main():
    a = 16807
    prev_a = 883
    b = 48271
    prev_b = 879
    base = 2147483647

    judge = 0
    for i in range(40000000):
        prev_a = (prev_a * a) % base
        prev_b = (prev_b * b) % base
        if prev_a % 65536 == prev_b % 65536:
            judge += 1

    print(judge)

main()
