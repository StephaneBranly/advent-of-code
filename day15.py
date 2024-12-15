from fileinput import input
import re, os, math

dirs = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

map, moves, y, x = [], None, 0, 0
for i, line in enumerate(input()):
    if moves != None:
        moves += line.replace('\n', '')
    elif line == '\n': moves = ''
    else:
        map.append([l for l in line.replace('\n', '')])
        if '@' in line:
            y, x = i, line.index('@')

for move in moves:
    dy, dx = dirs[move]
    new_y, new_x = y + dy, x + dx
    # print(move)
    while new_y >= 0 and new_y < len(map) and new_x >= 0 and new_x < len(map[0]):
        if map[new_y][new_x] == '.':
            map[new_y] = [map[y + dy][x + dx] if j == new_x else i for j, i in enumerate(map[new_y])]
            map[y] = ['.' if j == x else i for j, i in enumerate(map[y])]
            map[y + dy] = ['@' if j == x + dx else i for j, i in enumerate(map[y + dy])]
            new_x = -1
            y, x = y + dy, x + dx
        elif map[new_y][new_x] == '#':
            new_x = -1
        else:
            new_y += dy
            new_x += dx

    # [print(''.join(l)) for l in map]

sum = 0
for y, l in enumerate(map):
    for x, c in enumerate(l):
        if c == 'O': sum += 100 * y + x
print(map, moves, y,x, sum)