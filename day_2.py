levels = []
with open('./inputs/aoc_2.txt','r') as f:
    for line in f:
        levels.append([int(x) for x in line.split()])


# --------------- PART 1 -----------------
def level_is_safe(level):
    diff = [(y-x) for (x,y) in zip(level[:-1],level[1:])]
    if not (all(d<0 for d in diff) or all(d>0 for d in diff)):
        return False
    return all(1 <= abs(d) <= 3 for d in diff)

# count = 0
# for l in levels:
#     if level_is_safe(l):
#         count += 1
# print(count)

# --------------- PART 2 -----------------
count = 0
for l in levels:
    for i in range(len(l)):
        candidate = l[:i] + l[i+1:]
        if level_is_safe(candidate):
            count += 1
            break
print(count)