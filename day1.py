from fileinput import input
import os

l1, l2 = [], []
for line in input():
    a1, a2 = line.split('   ')
    l1.append(int(a1)), l2.append(int(a2.replace('\n', '')))
    
if int(os.environ.get('part', 1)) <= 1: # part 1
    s = sum([abs(a-b) for a,b in zip(sorted(l1), sorted(l2))])
else: # part 2
    s = sum(a * l2.count(a) for a in l1)
print(s)