"""
Advent of Code 2025, day 4
"""
import aoc_lib as aoc
from copy import deepcopy

matrix = aoc.matrix_from_file('input_04.txt')

aoc.TableCell.max_row = len(matrix)
aoc.TableCell.max_col = len(matrix[0])

total = 0
for tc in aoc.TableCell.iterate():
    if matrix[tc.row][tc.col] == '@':
        neighbours = tc.neighbours()
        rolls = 0
        for n in neighbours:
            if matrix[n.row][n.col] == '@':
                rolls += 1
        if rolls < 4:
            total += 1

print('answer part 1 :', total)

# part two

def remove_rolls():
    new_matrix = deepcopy(matrix)
    total = 0
    for tc in aoc.TableCell.iterate():
        if matrix[tc.row][tc.col] == '@':
            neighbours = tc.neighbours()
            rolls = 0
            for n in neighbours:
                if matrix[n.row][n.col] == '@':
                    rolls += 1
            if rolls < 4:
                total += 1
                new_matrix[tc.row][tc.col] = '.'

    return total, new_matrix

total_rolls_removed = 0
removed = -1
while removed != 0:
    removed, matrix = remove_rolls()
    total_rolls_removed += removed

print('answer part 2 :', total_rolls_removed)

