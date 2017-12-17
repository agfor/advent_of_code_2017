#!/usr/bin/env python3

from part_1 import circular_sum

def half_rotated_sum(data):
    return circular_sum(data, len(data) // 2)

if __name__ == "__main__":
    print(half_rotated_sum(open("input").read().strip()))
