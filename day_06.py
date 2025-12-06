"""
Advent of Code 2025, day 6
"""
import aoc_lib as aoc

from operator import __mul__
from operator import __add__
from functools import reduce

lines = aoc.lines_from_file('input_06.txt')

matrix = []
for line in lines:
    matrix.append(line.split())

n_rows = len(matrix)      # 5
n_cols = len(matrix[0])   # 1000

# let's seperate the operators, transpose the matrix and convert to int's
operators = ['' for _ in range(n_cols)]
numbers = [[0 for _ in range(n_rows-1)] for _ in range(n_cols)]

for col in range(n_cols):
    for row in range(n_rows-1):
        numbers[col][row] = int(matrix[row][col])
    operators[col] = matrix[-1][col]

answers = []
for col in range(n_cols):
    if operators[col] == '*':
        answers.append(reduce(__mul__, numbers[col]))
    else:
        answers.append(reduce(__add__, numbers[col]))

print('answer part 1 :', sum(answers))

# part two

# hmm....
# - we have to re-interpret our input lines
# - for convenience we append a space to the input lines
# - operators list is still valid

lines = [line + ' ' for line in lines]

col = 0
lines_col = 0
numbers = []
col_numbers = []

while True:
    word = "".join([lines[row][lines_col] for row in range(n_rows-1)])
    #print(word)
    if word.split() == []: # end marker
        col += 1
        numbers.append(col_numbers)
        col_numbers = []
        if col == n_cols:
            break
    else:
        number = int(word)
        col_numbers.append(number)
    lines_col += 1

# and we end in the same way as part 1
answers = []
for col in range(n_cols):
    if operators[col] == '*':
        answers.append(reduce(__mul__, numbers[col]))
    else:
        answers.append(reduce(__add__, numbers[col]))

print('answer part 2 :', sum(answers))

