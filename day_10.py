"""
Advent of Code 2025, day 10
"""
import aoc_lib as aoc
from collections import Counter, namedtuple
from itertools import combinations

lines = aoc.lines_from_file('input_10.txt')

# hmmm, eerst maar eens in wat handige data structuren fietsen....

Machine = namedtuple("Machine", "final buttons joltages")

machines = []
lengths = []
button_lengths = []
for line in lines:
    # split lines in final state, buttons and joltages, strip brackets
    parts = line.split(' ')
    final = [int(s=='#') for s in parts[0][1:-1]]  # make it bools..., no no 1's and 0's
    joltages = [int(s) for s in parts[-1][1:-1].split(',')]
    # let's check...
    assert len(final)  == len(joltages)
    lengths.append(len(final))
    # now the buttons....
    buttons = [[int(s) for s in part[1:-1].split(',')] for part in parts[1:-1]]
    button_lengths.append(len(buttons))
    # lets change the button definition
    for i, button in enumerate(buttons):
        new_button = [0] * len(final)
        for light_no in button:
            new_button[light_no] = 1
        buttons[i] = new_button

    machines.append(Machine(final, buttons, joltages))

print("lengths summary:", Counter(lengths))

# en dan weer even denken... :
# - het heeft geen nut om twee keer op dezelfde knop te drukken
# - volgorde maakt niet uit
# - we hebben max 10 knoppen, 2^10 = 1024 => brute-force is do-able
# dan maar wat functies tiepen

def add_button_to_state(state, button):
    return [s+b for s,b in zip(state, button)]

def digitize_state(state):
    return [s % 2  for s in state]

def how_many_binary_ones(i):
    return Counter(bin(i)[2:])['1']

# en weer door....

print("button_lengths summary:", Counter(button_lengths))

# oh shit, niet opgelet we hebben ook vijf gevallen met 13 knoppen...
# 2^13 = 8192.... oke  ook nog do-able

button_pushes_per_machine = [0] * len(machines)
for i_machine, machine in enumerate(machines):
    print('======== ', i_machine, ' =========')
    machine_mins = []
    l = len(machine.buttons)
    for n_push in range(1, l+1):
        print('---- ', n_push, ' -----')
        we_are_done = False
        for button_combos in combinations(range(l), n_push):
            state = [0] * len(machine.final)
            print(button_combos)
            for button in button_combos:
                state = add_button_to_state(state, machine.buttons[button])
                state = digitize_state(state)
                print(state)
                if state == machine.final:
                    print(i_machine, buttons, machine.buttons, buttons, state, machine.final)
                    we_are_done = True
                    button_pushes_per_machine[i_machine] = n_push
                    break       
        if we_are_done:
            break
            
print(button_pushes_per_machine, sum(button_pushes_per_machine))

print('answer part 1 :', sum(button_pushes_per_machine))

# part two

print('answer part 2 :', )


