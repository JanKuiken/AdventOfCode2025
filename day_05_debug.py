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

n_pos = 0
n_eq  = 0
n_neg = 0
for fr in fresh_ranges:
    if fr.stop >  fr.start: n_pos += 1
    if fr.stop == fr.start: n_eq += 1
    if fr.stop <  fr.start: n_neg += 1
print(n_pos, n_eq, n_neg)


invalid = Range(-1,-2)  # btw has invalid length 0

def length(r):
    return r.stop - r.start + 1

def total_length():
    return sum([length(fr) for fr in fresh_ranges])

def remove_invalids():
    global fresh_ranges
    while invalid in fresh_ranges:
        fresh_ranges.remove(invalid)

def remove_duplicates():
    global fresh_ranges
    fresh_ranges = list(set(fresh_ranges))

def have_overlap(r1, r2):
    return (   (r2.start >= r1.start and r2.start <= r1.stop)
            or (r2.stop  >= r1.start and r2.stop  <= r1.stop)
            or (r2.start <= r1.start and r2.stop  >= r1.stop)
            or (r1.start <= r2.start and r1.stop  >= r2.stop))

def overlap_count():
    N = len(fresh_ranges)
    count = 0
    for i1 in range(0, N-1):
        for i2 in range(i1+1, N):
            if have_overlap(fresh_ranges[i1], fresh_ranges[i2]):
                count += 1
    return count

def merge(r1, r2):
    # only call this if r1 and r2 have overlap
    min_start = min(r1.start, r2.start)
    max_stop  = max(r1.stop, r2.stop)
    return Range(min_start, max_stop)

print(len(fresh_ranges), total_length(), overlap_count())
remove_duplicates()
print(len(fresh_ranges), total_length(), overlap_count())

# like a bubble sort on ranges
N = len(fresh_ranges)
for i1 in range(0, N-1):
    for i2 in range(i1+1, N):
        if have_overlap(fresh_ranges[i1], fresh_ranges[i2]):
            merged = merge(fresh_ranges[i1], fresh_ranges[i2])
            fresh_ranges[i1] = invalid
            fresh_ranges[i2] = merged

print(len(fresh_ranges), total_length(), overlap_count())
remove_invalids()
print(len(fresh_ranges), total_length(), overlap_count())

# 347017202694462 is too high
print('answer part 2 :', total_length())



