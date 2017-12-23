#!/usr/bin/env pypy


def swap_rows(thing):
    if len(thing) == 4:
        return thing[2:] + thing[:2]
    else:
        return thing[6:] + thing[3:6] + thing[:3]
def swap_cols(thing):
    if len(thing) == 4:
        return thing[:2][::-1] + thing[2:][::-1]
    else:
        return thing[:3][::-1] + thing[3:6][::-1] + thing[6:][::-1]
def flip(thing):
    if len(thing) == 4:
        return thing[::2] + thing[1::2]
    else:
        return thing[::3] + thing[1::3] + thing[2::3]

def flips(thing):
    yield thing
    yield swap_rows(thing)
    yield swap_cols(thing)
    yield swap_rows(swap_cols(thing))
    yield flip(thing)
    yield flip(swap_rows(thing))
    yield flip(swap_cols(thing))
    yield flip(swap_rows(swap_cols(thing)))

patterns = {}
for i in range(2**9):
    thing = "{0:09b}".format(i).replace("0", ".").replace("1", "#")
    patterns[thing] = min(flips(thing))
for i in range(2**4):
    thing = "{0:04b}".format(i).replace("0", ".").replace("1", "#")
    patterns[thing] = min(flips(thing))

rules = [[item.replace("/", "") for item in line.strip().split(" => ")] for line in open("input")]
rules = {patterns[key]: value for key, value in rules}

def morph(pattern):
    if len(pattern) < 10:
        new_pattern = rules[patterns[pattern]]
    elif len(pattern) % 2 == 0:
        width = int(len(pattern)**0.5)
        new_pattern = [[] for _ in range((width * 3) // 2)]
        for k in range(0, width, 2):
            for i in range(0, width, 2):
              subpattern = pattern[i + width * k] + pattern[i + 1 + width * k] + pattern[i + width + width * k] + pattern[i + width + 1 + width * k]
              subpattern = morph(subpattern)
              new_pattern[3 * k//2].append(subpattern[:3])
              new_pattern[3 * k//2 + 1].append(subpattern[3:6])
              new_pattern[3 * k//2 + 2].append(subpattern[6:])
        new_pattern = "".join("".join(row) for row in new_pattern)
    else:
        width = int(len(pattern)**0.5)
        new_pattern = [[] for _ in range((width * 4) // 3)]
        for k in range(0, width, 3):
            for i in range(0, width, 3):
              subpattern = pattern[i + width * k] + pattern[i + 1 + width * k] + pattern[i + 2 + width * k]
              subpattern += pattern[i + width + width * k] + pattern[i + 1 + width + width * k] + pattern[i + 2 + width + width * k]
              subpattern += pattern[i + 2*width + width * k] + pattern[i + 1 + 2*width + width * k] + pattern[i + 2 + 2*width + width * k]
              subpattern = morph(subpattern)
              new_pattern[4 * k//3].append(subpattern[:4])
              new_pattern[4 * k//3 + 1].append(subpattern[4:8])
              new_pattern[4 * k//3 + 2].append(subpattern[8:12])
              new_pattern[4 * k//3 + 3].append(subpattern[12:])
        new_pattern = "".join("".join(row) for row in new_pattern)
    return new_pattern

pattern = """.#...####"""

for i in range(1, 18 + 1):
    pattern = morph(pattern)
    print(i, sum(1 for char in pattern if char == "#"))
