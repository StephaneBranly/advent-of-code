from fileinput import input
import os, re

step_1 = int(os.environ.get('part', 1)) <= 1

antennas = {}
map = [line.replace('\n', '') for line in input()]
antinodes_map = [[0] * len(l) for l in map]
def check_antinodes(new_antenna, antennas, antinodes_map):
    for antenna in antennas:
        v = (new_antenna[0] - antenna[0], new_antenna[1] - antenna[1])
        for ref, dir in [(new_antenna, v), (antenna, (v[0] * -1, v[1] * -1))]:
            valid, d = True, 1 if step_1 else 0
            while valid:
                y, x = ref[0] + d * dir[0],  ref[1] + d * dir[1]
                if y >= 0 and y < len(antinodes_map) and x >= 0 and x < len(antinodes_map[0]):
                    antinodes_map[y][x] = 1
                else:
                    valid = False
                if step_1: valid = False
                d += 1

for y, line in enumerate(map):
    new_antennas = [(m.group(0), m.start()) for m in re.finditer('[A-Za-z\\d]', line)]
    for type, x in new_antennas:
        check_antinodes((y, x), antennas.get(type, []), antinodes_map)
        antennas[type] = antennas.get(type, []) + [(y, x)]

print(sum([sum(l) for l in antinodes_map]))
