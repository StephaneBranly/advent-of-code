from fileinput import input
import re, os
import numpy as np
machines = [{'A': {}, 'B': {}, 'prize': {}}]

sum, d = 0, 0 if int(os.environ.get('part', 1)) <= 1 else 10000000000000
for line in input():
    match = re.search(r"Button (A|B): X\+(\d+), Y\+(\d+)", line)
    if match:
        machines[-1][match.group(1)]['X'] = int(match.group(2))
        machines[-1][match.group(1)]['Y'] = int(match.group(3))
    match = re.search(r"Prize: X=(\d+), Y=(\d+)", line)
    if match:
        machines[-1]['prize']['X'] = int(match.group(1)) + d
        machines[-1]['prize']['Y'] = int(match.group(2)) + d
        m = machines[-1]
        machines.append({'A': {}, 'B': {}, 'prize': {}})
        [s1, s2] = np.linalg.solve([[m['A']['X'], m['B']['X']], [m['A']['Y'], m['B']['Y']]],[m['prize']['X'], m['prize']['Y']])
        if (int(round(s1,2)) == round(s1,2)) and (int(round(s2,2)) == round(s2,2)):
            sum += round(s1, 0) * 3 + round(s2, 0)

print(int(sum))