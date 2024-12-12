from fileinput import input
import os

blinks = {}
stones = input().readline()

def blink(stone, r = 25):
    if not r: return 1

    if (stone, r) in blinks: return blinks[(stone, r)]

    if int(stone) == 0:
        res = blink('1', r-1)
    elif len(stone) % 2 == 0:
        res = blink(str(int(stone[:int(len(stone)/2)])), r-1) + blink(str(int(stone[int(len(stone)/2):])), r-1)
    else:
        res = blink(str(int(stone) * 2024), r-1)

    blinks[(stone, r)] = res
    return res

print(sum([blink(d, 75 if int(os.environ.get('part', 1)) > 1 else 25) for d in stones.split(' ')]))