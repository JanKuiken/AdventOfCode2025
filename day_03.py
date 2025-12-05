"""
Advent of Code 2025, day 3
"""
import aoc_lib as aoc

lines = aoc.lines_from_file('input_03.txt')


def highest_jolta(line):
    
    l = len(line)
    first_highest_digit = 0
    first_highest_pos = 0
    
    for i in range(0, l-1):
        if int(line[i]) > first_highest_digit:
            first_highest_digit = int(line[i])
            first_highest_pos = i

    start = first_highest_pos + 1
    second_highest_digit = 0
    second_highest_pos = 0

    for i in range(start, l):
        if int(line[i]) > second_highest_digit:
            second_highest_digit = int(line[i])
            second_highest_pos = i

    #print(first_highest_pos, second_highest_pos)
    highest = int(str(first_highest_digit) + str(second_highest_digit))
    #print(highest)
    return highest


total = sum([highest_jolta(line) for line in lines])
    
print('answer part 1 :', total)

# part two

def highest_jolta2(n_digits, line):
    """More general version of previous function"""
    
    l = len(line)
    start = 0
    
    highest_digits = []
    
    for digit_n in range(n_digits):
        highest = 0
        stop = l - n_digits + digit_n 
        for i in range(start, stop + 1):
            if int(line[i]) > highest:
                highest = int(line[i])
                start = i + 1
        highest_digits.append(highest)
    
    return int("".join([str(i) for i in highest_digits]))

N = 2
total = sum([highest_jolta2(N, line) for line in lines])
print('answer part 1 (check):', total)

N = 12
total = sum([highest_jolta2(N, line) for line in lines])
print('answer part 2 :', total)

