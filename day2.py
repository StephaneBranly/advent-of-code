from fileinput import input
import os

def check_rules(diff):
    return all([abs(d) in [1,2,3] for d in diff]) and (all([d<0 for d in diff]) or all([d>0 for d in diff]))

valid_reports = 0
for report in input():
    levels = report.replace('\n','').split(' ')
    diff_levels = [int(a) - int(b) for a, b in zip(levels, levels[1:])]

    if int(os.environ.get('part', 1)) <= 1: # part 1
        if check_rules(diff_levels):
            valid_reports += 1
    else: # part 2
        if check_rules(diff_levels): valid_reports += 1
        else:
            for i in range(len(levels)):
                modified_levels = [d for ind, d in enumerate(levels) if i != ind]
                diff_levels = [int(a) - int(b) for a, b in zip(modified_levels, modified_levels[1:])]
                if check_rules(diff_levels):
                    valid_reports += 1
                    break

print(valid_reports)