from fileinput import input
import os, re

r = 0

if int(os.environ.get('part', 1)) <= 1: # part 1
    for line in input():
        mults = re.finditer('mul\\((\\d+),(\\d+)\\)', line)
        r += sum([int(m.group(1)) * int(m.group(2)) for m in mults])
else: # part 2
    instructions = [(-1, True)]
    for line in input():
        instructions = [(-1, instructions[-1][1])] + [(m.start(), m.group(1) == 'do()') for m in re.finditer("(do\\(\\)|don't\\(\\))", line)]
        mults = re.finditer('mul\\((\\d+),(\\d+)\\)', line)
        r += sum([int(m.group(1)) * int(m.group(2)) for m in mults if [exe for start, exe in instructions if start < m.start()][-1]])
print(r)