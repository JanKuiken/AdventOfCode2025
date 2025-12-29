"""
Advent of Code 2025, day 11
"""
import aoc_lib as aoc

lines = aoc.lines_from_file('input_11.txt')

g = {}   # dit wordt de 'graph'
for line in lines:
    k,v = line.split(': ')
    vs = v.split(' ')
    g[k] = vs

count = 0

def walk(node):
    global count
    if node == 'out':
        count += 1
    else:
        for child in g[node]:
            walk(child)

walk('you')

print('answer part 1 :', count)

# part two

print('answer part 2 :', )


