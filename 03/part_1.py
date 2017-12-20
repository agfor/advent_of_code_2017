#!/usr/bin/env python3

print("""Did this one using the REPL as a calculator.
Upper left diagonal are even squares + 1, bottom right are odd squares.
Figure out which squares you're between,
then which direction is the closest axis by seeing which quarter of the area between you're in.
Then walk (sqrt // 2) + distance to axis.

>>> 368078
368078
>>> 605**2
366025
>>> 607**2
368449
>>> 607**2 - 605**2
2424
>>> 605**2 + 2424 / 4
366631.0
>>> 368078
368078
>>> 605**2 + 2424 // 3
366833
>>> 605**2 + 2424 * (3 / 4)
367843.0
>>> 605**2 + 2424 / 8
366328.0
>>> 2424 / 8
303.0
>>> 368078 + 303
368381
>>> 607**2
368449
>>> 607**2 - 303
368146
>>> 607**2 - 303 - 368078
68
>>> 607 - 1
606
>>> 606 / 2
303.0
>>> 303 + 68
371
""")
