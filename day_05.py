"""
Advent of Code 2025, day 5
"""
import aoc_lib as aoc
from collections import namedtuple
Range = namedtuple("Range", "start stop")

lines = aoc.lines_from_file('input_05.txt')
#lines = aoc.lines_from_file('test_input_05.txt')

fresh_ranges_str, ingredients_str = aoc.split_on_empty_string(lines)
fresh_ranges = []
for frs in fresh_ranges_str:
    start, stop = frs.split('-')
    fresh_ranges.append(Range(int(start), int(stop)))
ingredients = [int(id) for id in ingredients_str]

def is_fresh(id):
    for fr in fresh_ranges:
        if id >= fr.start and id <= fr.stop:
            return True
    return False

total_fresh = 0
for id in ingredients:
    if is_fresh(id):
        total_fresh += 1

print('answer part 1 :', total_fresh)

# part two

# hmm we have to remove the overlaps...
# - stop is always greater or equal start
# - we have ranges of length 1
# - we do have identical ranges:
#   len(fresh_ranges)        => 181
#   len(set(fresh_ranges))   => 172

# let's write some tools

def length(r):
    return r.stop - r.start + 1

def total_length():
    return sum([length(fr) for fr in fresh_ranges])

INVALID = Range(-1,-2)  # btw. invalid has length 0

def have_overlap(r1, r2):
    return (   (r2.start >= r1.start and r2.start <= r1.stop)
            or (r2.stop  >= r1.start and r2.stop  <= r1.stop)
            or (r2.start <= r1.start and r2.stop  >= r1.stop)
            or (r1.start <= r2.start and r1.stop  >= r2.stop))
            
def merge(r1, r2):
    # only call this if r1 and r2 have overlap
    min_start = min(r1.start, r2.start)
    max_stop  = max(r1.stop, r2.stop)
    return Range(min_start, max_stop)

# like a bubble sort on ranges
N = len(fresh_ranges)
for i1 in range(0, N-1):
    for i2 in range(i1+1, N):
        if have_overlap(fresh_ranges[i1], fresh_ranges[i2]):
            merged = merge(fresh_ranges[i1], fresh_ranges[i2])
            fresh_ranges[i1] = INVALID
            fresh_ranges[i2] = merged

print('answer part 2 :', total_length())

