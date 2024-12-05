from fileinput import input
import os, math

constraints, instructions, sum = {}, [], 0
for line in input():
    line = line.replace('\n','')
    if '|' in line:
        left, right = line.split('|')
        constraints[int(left)] = constraints.get(int(left), []) + [int(right)]
    elif ',' in line:
        instructions.append([int(p) for p in line.split(',')])
  
def is_valid_instruction(instruction):
    for index, page in enumerate(instruction):
        for next_index, next_page in enumerate(instruction[index+1:]):
            if page in constraints.get(next_page, []):
                return False, index, next_index + index + 1
    return True, index, next_index + index + 1

for instruction in instructions:
    valid, i, j = is_valid_instruction(instruction)
    if int(os.environ.get('part', 1)) <= 1 and valid: # part 1
        sum += instruction[math.floor(len(instruction) / 2)]
    elif int(os.environ.get('part', 1)) > 1 and not valid:
        instruction = instruction.copy()
        while not valid: # we suppose that swapping will lead to a valid solution
            instruction[i], instruction[j] = instruction[j], instruction[i]
            valid, i, j = is_valid_instruction(instruction)
        sum += instruction[math.floor(len(instruction) / 2)]

print(sum)