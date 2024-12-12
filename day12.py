from fileinput import input
import os

map, visited = [], []
for line in input():
    map += [line.replace('\n','')]

def is_valid(y,x):
    return not (x < 0 or x >= len(map[0]) or y < 0 or y >= len(map))

dirs = {
    't': (-1, 0),
    'b': (1, 0),
    'l': (0, -1),
    'r': (0, 1)
}

def visit(y, x):
    if (y, x) in visited: return [], 0
    visited.append((y,x))
    fences, area = [], 1
    for dir, (dy, dx) in dirs.items():
        next_y, next_x = dy + y, dx + x
        if is_valid(next_y, next_x) and map[next_y][next_x] == map[y][x]:
            if (next_y, next_x) not in visited:
                next_fences, next_area = visit(next_y, next_x)
                area   += next_area
                fences += next_fences
        elif dx < 0:
            fences.append((y, x, 'l'))
        elif dx > 0:
            fences.append((y, x, 'r'))
        elif dy < 0:
            fences.append((y, x, 't'))
        elif dy > 0:
            fences.append((y, x, 'b'))
        
    return fences, area

sum = 0
for y, l in enumerate(map):
    for x, c in enumerate(l):
        f, a = visit(y, x)
        if a:
            if int(os.environ.get('part', 1)) <= 1:
                sum += len(f) * a
            else:
                un = 0
                for dir, dy, dx in [('b', 0, 1), ('t', 0, 1), ('l', 1, 0), ('r', 1, 0)]:
                    for fence in [ff for ff in f if ff[2] == dir]:

                        if (    fence[0] + dy,
                                fence[1] + dx,
                                dir
                        ) not in f:
                            un += 1
                sum += un * a

print(sum)