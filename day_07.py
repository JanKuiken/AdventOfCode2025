"""
Advent of Code 2025, day 7
"""
import aoc_lib as aoc

matrix = aoc.matrix_from_file('input_07.txt')

n_rows = len(matrix)      
n_cols = len(matrix[0])   

splits = 0

for row in range(1, n_rows):
    for col in range(n_cols):
        if matrix[row][col] == '.':
            if matrix[row-1][col] == "S" or matrix[row-1][col] == "|":
                matrix[row][col] = '|'
        if matrix[row][col] == '^':
            if matrix[row-1][col] == "|":
                matrix[row][col-1] = '|'
                matrix[row][col+1] = '|'
                splits += 1

aoc.print_matrix(matrix)

print('answer part 1 :', splits)

# part two

# we start from bottom to top
# we keep the filled matrix from part 1
# for each '|' and '^' we memorize the number of time lines
# from that point to the bottom, we store these values in a
# matrix of integers

times = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

# first the bottom row
for col in range(n_cols):
    if matrix[n_rows-1][col] == '|':
        times[n_rows-1][col] = 1

# then the others from 2nd row from bottom till top
for row in range(n_rows-2, 0, -1):
    # eerst de '|'
    for col in range(n_cols):
        if matrix[row][col] == '|':
            # waarde van de '|' of '^' eronder
            times[row][col] = times[row+1][col]
    for col in range(n_cols):
        if matrix[row][col] == '^':
            # som van de waardes van de '|' links en rechts
            times[row][col] = times[row][col-1] + times[row][col+1]

# answer is the single non zero value of row 1
print('answer part 2 :', sum(times[1]))

