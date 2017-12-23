#!/usr/bin/env pypy

def main():
    a = b = c = d = e = f = g = h = 0
    a = 1
    b = c = 65
    if a != 0:
        b = b * 100 + 100000
        c = b + 17000
    f = 1
    d = 2
    e = 3
    g = 3 - b
    while True:
        if b % d == 0:
            f = 0
        d += 1
        g = d - b
        if g == 0:
            if f == 0:
                h += 1
            g = b - c
            if g == 0:
                return locals()
            b += 17
            f = 1
            d = 2
            e = 3
            g = 3 - b
        else:
            e = 3
            g = d * 2 - b
            if g == 0:
                f = 0
            g = 3 - b

print(main())
