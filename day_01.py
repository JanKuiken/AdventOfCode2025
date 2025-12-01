"""
Advent of Code 2025, day 1
"""

import aoc_lib as aoc

lines = aoc.lines_from_file("input_01.txt")

dirs = []
amount = []
for line in lines:
    dirs.append(line[0])
    amount.append(int(line[1:]))

dial = 50
zeros = 0
for d,a in zip(dirs, amount):
    if d == 'R':
        dial += a
    else:
        dial -= a
    passes += abs(dial//100)
    dial %= 100
    if dial == 0:
        zeros += 1

print('oplossing  1 :', zeros)

