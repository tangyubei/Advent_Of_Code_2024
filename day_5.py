from collections import defaultdict
import math

r_test = []
with open('./inputs/aoc_5_test.txt', 'r') as f:
    for line in f:
        r_test.append([int(x) for x in line.rstrip().split('|')])

u_test = [[75,47,61,53,29],
[97,61,53,29,13],
[75,29,13],
[75,97,47,61,53],
[61,13,29],
[97,13,75,29,47]]

r_data = []
with open('./inputs/aoc_5_part1.txt', 'r') as f:
    for line in f:
        r_data.append([int(x) for x in line.rstrip().split('|')])

u_data = []
with open('./inputs/aoc_5_part2.txt', 'r') as g:
    for line in g:
        u_data.append([int(x) for x in line.rstrip().split(',')])

# --------------- PART 1 -----------------

def dict_of_sets(rules):
    r_dict = defaultdict(set)
    for r in rules:
        r_dict[r[0]].add(r[1])
    return r_dict

def valid_update(update, rules_dict):
    for i in range(len(update)-1):
        if not set(update[i+1:]).issubset(rules_dict[update[i]]):
            return False
    return True

def calc_midp(update):
    return update[math.floor(len(update)/2)]

def get_p1_result(rules, updates):
    result = 0
    rules_dict = dict_of_sets(rules)
    for update in updates:
        if valid_update(update, rules_dict):
            result += calc_midp(update)
    return result
#
# print(get_p1_result(r_data, u_data))

# --------------- PART 2 -----------------
d_test = dict_of_sets(r_test)
def change_update(update, rules_dict):
    for i in range(len(update)-2,-1,-1):
        pivot = update[i]
        if not valid_update(update[i:], rules_dict):
            for j in range(i+1, len(update)):
                if not valid_update([pivot,update[j]], rules_dict):
                    update[i], update[j] = update[j], update[i]
                    i = i + 1
    return update

def get_p2_result(rules, updates):
    result = 0
    rules_dict = dict_of_sets(rules)
    for update in updates:
        if not valid_update(update, rules_dict):
            new_update = change_update(update, rules_dict)
            result += calc_midp(new_update)
    return result

print(get_p2_result(r_data, u_data))