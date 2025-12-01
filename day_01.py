"""
Advent of Code 2025, day 1
"""
import aoc_lib as aoc

lines = aoc.lines_from_file('input_01.txt')

dirs = []
amount = []
for line in lines:
    dirs.append(line[0])
    amount.append(int(line[1:]))

dial = 50
zeros = 0
passes = 0 # for part2

for d,a in zip(dirs, amount):
    if d == 'R':
        dial += a
    else:
        dial -= a
    passes += int(abs(dial//100))
    dial %= 100
    if dial == 0:
        zeros += 1

print('answer part 1 :', zeros)
print('answer part 2 :', passes)

# hmm, the answer for part 2 (6513) is wrong, dunno why... 
# (calculation of passes was too fancy...?)
# let's simulate it more explicitly...

dial = 50
zeros = 0

for d,a in zip(dirs, amount):
    for _ in range(a):
        if d == 'R': 
            dial += 1
            if dial == 100:
                dial = 0
                zeros += 1
        else: # d == 'L'
            dial -= 1
            if dial == 0:
                zeros += 1
            if dial == -1:
                dial = 99
 
print('answer part 2 :', zeros)

