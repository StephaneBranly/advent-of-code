from fileinput import input
import os

map, transitions = [], {}
for line in input():
    map += [line.replace('\n','')]

def explore_cell(y, x):
    if (y, x) in transitions: return transitions[(y, x)]
    nexts = []
    if map[y][x] == '9': nexts = [(y, x)]
    elif map[y][x] == '.': pass
    else: 
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            next_y, next_x = dy + y, dx + x
            if next_x < 0 or next_x >= len(map[0]) or next_y < 0 or next_y >= len(map):
                pass
            elif map[next_y][next_x] != '.' and int(map[y][x]) + 1 == int(map[next_y][next_x]):
                nexts += explore_cell(next_y, next_x)
    if int(os.environ.get('part', 1)) > 1: # part 2
        nexts = list(set(nexts))
    transitions[(y, x)] = nexts
    return nexts

sum = 0
for y, l in enumerate(map):
    for x, c in enumerate(l):
        if c == '0':
            sum += len(explore_cell(y, x))

print(sum)