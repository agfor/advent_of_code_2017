#!/usr/bin/env python3

import re

data = [re.findall("\d+", line) for line in open("input")]

result = set(data[0])
size = 0
while len(result) > size:
    size = len(result)
    for line in data:
        if any(item in result for item in line):
            result.update(line)

print(len(result))
