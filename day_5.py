from collections import defaultdict
import math

ordering_rules, pages_to_produce_updates = [], []
with open('inputs/aoc_5_part1.txt', 'r') as file:
    for line in file:
        ordering_rules.append(line.rstrip('\n'))

with open('inputs/aoc_5_part2.txt', 'r') as file:
    for line in file:
        pages_to_produce_updates.append(list(map(int, line.rstrip().split(','))))


test_page_ordering_rules = ["47|53",
"97|13",
"97|61",
"97|47",
"75|29",
"61|13",
"75|53",
"29|13",
"97|29",
"53|29",
"61|53",
                            "97|53",
                            "61|29",
                            "47|13",
                            "75|47",
                            "97|75",
                            "47|61",
                            "75|61",
                            "47|29",
                            "75|13",
                            "53|13"]

test_pages_to_produce_each_update = [[75, 47, 61, 53, 29],
                                     [97,61,53,29,13],
                                     [75,29,13],
                                     [75,97,47,61,53],
                                     [61,13,29],
                                     [97,13,75,29,47]]
#
def check_updates(rules, updates):
    ordering_rules_dict = defaultdict(set)
    for rule in rules:
        processed_rule = [int(x) for x in rule.split("|")]
        ordering_rules_dict[processed_rule[0]].add(processed_rule[1])
    return ordering_rules_dict

def get_updates(ordering_rules_dict, updates):
    good_updates, bad_updates = [], []
    for update in updates:
        update_is_good = True
        for i in range(len(update)-1):
            if not set(update[i+1:]).issubset(ordering_rules_dict[update[i]]):
                update_is_good = False
                break
        if update_is_good:
            good_updates.append(update)
        else:
            bad_updates.append(update)
    return [good_updates, bad_updates]

def sum_update_middles(updates):
    result = 0
    for update in updates:
        result += update[math.floor(len(update)/2)]
    return result

ordering_rules_dict = check_updates(ordering_rules, pages_to_produce_updates)
[good_updates, bad_updates] = get_updates(ordering_rules_dict, pages_to_produce_updates)
print(sum_update_middles(good_updates))

def fix_updates(dictionary, updates):
    print(dictionary)
    print(47 in dictionary[97])
    for update in updates:
        print(update)

        for i in range(len(update)-1):
            for j in range(i+1, len(update)-1):
                if update[j] not in dictionary[update[i]]:
                    update[i], update[j] = update[j], update[i]
        print(update)

test_ordering_rules_dict = check_updates(test_page_ordering_rules, test_pages_to_produce_each_update)
[test_good_updates, test_bad_updates] = get_updates(test_ordering_rules_dict, test_pages_to_produce_each_update)
print(sum_update_middles(test_good_updates))
print(fix_updates(test_ordering_rules_dict, test_bad_updates))

