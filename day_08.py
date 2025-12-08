"""
Advent of Code 2025, day 8
"""
import aoc_lib as aoc
from math import sqrt

lines = aoc.lines_from_file('input_08.txt')

boxes = []
for line in lines:
    x,y,z = line.split(',')
    x = int(x)
    y = int(y)
    z = int(z)
    boxes.append((x,y,z))

N = len(boxes)

distances = []
for i in range(0, N-2):
    for j in range(i+1, N):
        x1, y1, z1 = boxes[i] 
        x2, y2, z2 = boxes[j]
        dist = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        distances.append((dist,i,j))

distances.sort()

# networks is een list van lists met (sorted) indices
# we starten met : [ [0], [1], [2],.....,[999] ]
# als bijvoorbeeld index 17 en 321 ge-connect worden verdwijnen
# items die 17 en 321 bevatten en komt er een nieuwe die beide bevatten
# let's create networks and write some helper functions...

networks = [[i] for i in range(N)]

def find_networks_element_containing(i):
    for nw in networks:
        if i in nw:
            return nw
    raise ValueError("Oeps, index not found in global list variable network.")

def join_network_elements(i,j):
    global networks
    nw_i = find_networks_element_containing(i)
    nw_j = find_networks_element_containing(j)
    if nw_i != nw_j:
        networks.remove(nw_i)
        networks.remove(nw_j)
        combined = nw_i + nw_j
        combined = list(set(combined))   # remove doublures
        combined.sort()                  # sort the combined
        networks.append(combined)
    else:
        pass # nothing to be done

# ik denk dat we nu de ingredienten hebben, let's go
#   " connect together the 1000 pairs of junction boxes 
#     which are closest together. "
for dist, i, j in distances[:1000]:
    join_network_elements(i,j)

# sanity checks...
print('len(networks) : ', len(networks))
still_thousand = sum([len(nw) for nw in networks])
print('number of boxes in networks :', still_thousand)
assert still_thousand == N, "Oeps, we've lost boxes somewhere..."

# ok, let's find the answer...
len_networks = [len(nw) for nw in networks]
len_networks.sort(reverse=True)
answer_1 = len_networks[0] * len_networks[1] * len_networks[2]

print('answer part 1 :', answer_1)

# part two

# oke, we gaan door met korste afstanden verbinden totdat alles met elkaar
# verbonden is...

for dist, i, j in distances[1000:]:
    join_network_elements(i,j)
    if len(networks) == 1:
        print('Joeppie')
        print(boxes[i], boxes[j])
        print('answer part 2 :', boxes[i][0] * boxes[j][0])
        break


