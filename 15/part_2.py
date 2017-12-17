#!/usr/bin/env python3

def gen_a():
    a = 16807
    prev_a = 883
    base = 2147483647
    while True:
        prev_a = (prev_a * a) % base
        if prev_a % 4 == 0:
            yield prev_a

def gen_b():
    b = 48271
    prev_b = 879
    base = 2147483647
    while True:
        prev_b = (prev_b * b) % base
        if prev_b % 8 == 0:
            yield prev_b

def main():
    judge = 0
    a_seq = gen_a()
    b_seq = gen_b()
    for i in range(5000000):
        if next(a_seq) % 65536 == next(b_seq) % 65536:
            judge += 1

    print(judge)

main()
