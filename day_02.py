"""
Advent of Code 2025, day 2
"""
import aoc_lib as aoc

lines = aoc.lines_from_file('input_02.txt')
#lines = aoc.lines_from_file('test_input_02.txt')

# store in an appropriate data structure
line = lines[0] #
ranges_str = line.split(',')
ranges = []  # list of tuples with start/stop ID's
for rs in ranges_str:
    start, stop = rs.split('-')
    ranges.append((int(start), int(stop)))

# lets print out what we're dealing with...
print(ranges)
total = 0
max_len = 0
min_len = 99
for start, stop in ranges:
    total += stop - start + 1
    max_len = max(max_len, len(str(stop)))
    min_len = min(min_len, len(str(start)))
print(total, max_len, min_len)

# total = approx. two million => brute force is possible

def is_NOT_an_valid_ID(id):
    id_str = str(id)
    length = len(id_str)
    if length % 2 == 1:
        # ID's with odd digits length are always valid
        return False 
    front = id_str[: length // 2]
    back  = id_str[length // 2 :]
    return front == back

total_invalids = 0
for start, stop in ranges:
    for id in range(start, stop + 1):
        if is_NOT_an_valid_ID(id):
            total_invalids += id

print('answer part 1 :', total_invalids)

# part two

def is_NOT_an_valid_ID_part_two(id):
    str_id = str(id)
    len_id = len(str_id)
    checks = { 1 : [], 
               2 : [1],
               3 : [1],
               4 : [1,2],
               5 : [1],
               6 : [1,2,3],
               7 : [1],
               8 : [1,2,4],
               9 : [1,3],
               10: [1,2,5],
    }
    #print(id, len_id)
    for i in checks[len_id]:
        test_str = str_id[:i] * (len_id // i)
        #print(test_str_part, test_str, str_id)
        if test_str == str_id:
            return True
    return False

total_invalids = 0
max_len = 0
for start, stop in ranges:
    #print('----------------')
    for id in range(start, stop + 1):
        if is_NOT_an_valid_ID_part_two(id):
            total_invalids += id


# 41823587585 is too high
print('answer part 2 :', total_invalids)

