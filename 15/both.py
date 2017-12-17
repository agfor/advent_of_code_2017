#!/usr/bin/env pypy

def main():
    prev_a = 883
    prev_b = 879
    judge = 0
    for i in range(40000000):
        prev_a = (prev_a * 16807) % 2147483647
        prev_b = (prev_b * 48271) % 2147483647
        if prev_a % 65536 == prev_b % 65536:
            judge += 1

    print(judge)

    prev_a = 883
    prev_b = 879
    judge = 0
    for i in range(5000000):
        prev_a = (prev_a * 16807) % 2147483647
        while prev_a % 4 != 0:
            prev_a = (prev_a * 16807) % 2147483647

        prev_b = (prev_b * 48271) % 2147483647
        while prev_b % 8 != 0:
            prev_b = (prev_b * 48271) % 2147483647

        if prev_a % 65536 == prev_b % 65536:
            judge += 1

    print(judge)

main()
from time import time
start = time()
main()
print(time() - start)
