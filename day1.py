from fileinput import input

l1, l2 = [], []
for line in input():
    a1, a2 = line.split('   ')
    l1.append(int(a1)), l2.append(int(a2.replace('\n', '')))
    
if True: # step 1
    s = sum([abs(a-b) for a,b in zip(sorted(l1), sorted(l2))])
else: # step 2
    s = sum(a * l2.count(a) for a in l1)
print(s)