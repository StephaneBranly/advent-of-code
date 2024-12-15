from fileinput import input
import re, os, math

robots = []
i, h, w = 100, 103, 101
q1, q2, q3, q4 = 0, 0, 0, 0
for line in input():
    m = re.search(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
    robots.append(((int(m.group(2))+i*int(m.group(4)))%h, (int(m.group(1))+i*int(m.group(3)))%w, int(m.group(4)), int(m.group(3))))
    y, x, dy, dx = robots[-1]
    if y < math.floor(h / 2) and x < math.floor(w / 2): q1 += 1
    elif y < math.floor(h / 2) and x >= math.ceil(w / 2): q2 += 1
    elif y >= math.ceil(h / 2) and x < math.floor(w / 2): q3 += 1
    elif y >= math.ceil(h / 2) and x >= math.ceil(w / 2): q4 += 1


if int(os.environ.get('part', 1)) <= 1: # part 1
    print(q1 * q2 * q3 * q4)
else:
    inp = ''
    while inp != 'stop':
        print(i, end='\r')
        i+=1
        robots = [((y+dy)%h, (x+dx)%w, dy, dx) for y, x, dy, dx in robots]
        pos = [(a,b) for a,b,_,__ in robots]
        count = set(pos.count(i) for i in pos)
        if count == set([1]):
            inp = 'stop'
            print(i)
            for ii in range(h):
                for j in range(w):
                    if (ii, j) in pos:
                        print('1', end='')
                    else:
                        print('.', end='')
                print('')