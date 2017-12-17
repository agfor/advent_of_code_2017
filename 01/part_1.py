#!/usr/bin/env python3

def circular_sum(data, offset = 1):
    return sum(
            (int(d1) if d1 == d2 else 0)
                for d1, d2 in
                    zip(data, data[offset:] + data[:offset]))

if __name__ == "__main__":
    print(circular_sum(open("input").read().strip()))
