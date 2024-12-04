from fileinput import input
import os

map = [line.replace('\n','') for line in input()]
count = 0

if int(os.environ.get('part', 1)) <= 1: # part 1
    for i, line in enumerate(map):
        for j, cell in enumerate(line):
            if cell == 'X':
                for dx, dy in [(-1,-1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                    pos = [(i, j)]
                    valid = True
                    for di, l in enumerate('MAS'):
                        nx = i + dx * (di + 1)
                        ny = j + dy * (di + 1)
                        if nx < 0 or nx >= len(map) or ny < 0 or ny >= len(line) or map[nx][ny] != l:
                            valid = False
                            break
                    if valid: count += 1
else:
    for i, line in enumerate(map):
        for j, cell in enumerate(line):
            if cell == 'M':
                for dx, dy in [(-1,-1), (1, 1), (1, -1), (-1, 1)]:
                    nx = i + dx * 2
                    ny = j + dy * 2
                    if not (nx < 0 or nx >= len(map) or ny < 0 or ny >= len(line)) \
                    and map[i + dx][j + dy] == 'A' and map[nx][ny] == 'S' and ((map[i][ny] == 'M' and map[nx][j] == 'S') or (map[i][ny] == 'S' and map[nx][j] == 'M')):
                        count += 1/2
print(int(count))