from fileinput import input
import re

filesystem = input().readline()
print(filesystem)
space = [item for sub_list in [[int(i/2)] * int(d) if i % 2 == 0 else ['.'] * int(d) for i, d in enumerate(filesystem)] for item in sub_list]
continuer = True
last_digit = len(space) - 1
while continuer:
    while space[last_digit] == '.' and last_digit >= 0:
        last_digit -= 1
    if last_digit > 0 and last_digit > space.index('.'):
        space[space.index('.')], space[last_digit] = space[last_digit], space[space.index('.')]
    else: continuer = False

print(sum([int(d) * i for i, d in enumerate(space) if d != '.']))