from fileinput import input
import re, os

filesystem = input().readline()
space = [item for sub_list in [[str(int(i/2))] * int(d) if i % 2 == 0 else ['.'] * int(d) for i, d in enumerate(filesystem)] for item in sub_list]
continuer = True
last_digit = len(space) - 1
available_spaces = [(m.start(), m.end(), m.end() - m.start()) for m in re.finditer('(\\.)+', ''.join(['d' if i != '.' else '.' for i in space]))]

while continuer:
    while space[last_digit] == '.' and last_digit >= 0:
        last_digit -= 1
    
    if int(os.environ.get('part', 1)) <= 1:
        block_size = 1
    else:
        block_size = space.count(space[last_digit])

    compatible = [i for i, a in enumerate(available_spaces) if block_size <= a[2]]
    if len(compatible):
        available_space = available_spaces[compatible[0]]
        for i in range(block_size):
            space[available_space[0] + i], space[last_digit - i] = space[last_digit - i], space[available_space[0] + i]
        available_spaces[compatible[0]] = (available_space[0] + block_size, available_space[1], available_space[2] - block_size)
        
    last_digit -= block_size

    available_spaces = [a for a in available_spaces if a[1] < last_digit and a[2] > 0]
    if last_digit <= 0 or not len(available_spaces):
        continuer = False
    
print(sum([int(d) * i for i, d in enumerate(space) if d != '.']))