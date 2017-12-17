#!/usr/bin/env python3

import re

data = [re.findall("\d+", line) for line in open("input")]

total = 0
while data:
    total += 1
    new_data = data.copy()
    result = set(data[0])
    size = 0
    while len(result) > size:
        size = len(result)
        for line in data:
            if any(item in result for item in line):
                result.update(line)
                for i, other_line in enumerate(new_data):
                    if other_line == line:
                        del new_data[i]
    data = new_data

print(total)
