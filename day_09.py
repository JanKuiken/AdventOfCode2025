"""
Advent of Code 2025, day 9
"""
import aoc_lib as aoc
from collections import Counter, namedtuple

lines = aoc.lines_from_file('input_09.txt')

red_tiles = []
for line in lines:
    x,y = line.split(',')
    x = int(x)
    y = int(y)
    red_tiles.append((x,y))

N = len(red_tiles)  # not really a constant, but who cares

areas = []
for i in range(0, N-1):
    for j in range(i+1, N):
        x1, y1 = red_tiles[i] 
        x2, y2 = red_tiles[j]
        area = (x1-x2+1) * (y1-y2+1) 
        areas.append((area,i,j))

areas.sort(reverse=True)

print('answer part 1 :', areas[0][0])

# part two

print('answer part 2 :', )


