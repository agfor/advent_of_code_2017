#!/usr/bin/env python3

# Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1.
# Otherwise, increase it by 1 as before. 

from itertools import count

data = [int(line) for line in open("input")]
offset = 0

try:
    for i in count(0):
        new_offset = offset + data[offset]
        if data[offset] > 2:
            data[offset] -= 1
        else:
            data[offset] += 1
        offset = new_offset
except IndexError:
    print(i)
