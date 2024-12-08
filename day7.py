from fileinput import input
import os

def is_valid(test_value, sum, operands):
    if not len(operands):
        return test_value == sum
    if (sum > test_value):
        return False
    
    if is_valid(test_value, sum + operands[0], operands[1:]) or is_valid(test_value, sum * operands[0], operands[1:]):
        return True
    
    if int(os.environ.get('part', 1)) > 1: # part 2
        return is_valid(test_value, int(f'{sum}{operands[0]}'), operands[1:])
    return False

sum = 0
for line in input():
    test_value, operands = line.replace('\n', '').split(': ')
    operands = [int(o) for o in operands.split(' ')]
    if is_valid(int(test_value), 0, operands): sum += int(test_value)

print(sum)