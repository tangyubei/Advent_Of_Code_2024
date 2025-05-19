# --------------- PART 1 -----------------
testInput =[[ 7, 6, 4, 2, 1,],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]]

report = []
with open('./inputs/aoc_2.txt', 'r') as file:
    for line in file:
        newLine = [int(x) for x in line.split()]
        report.append(newLine)
#
# numDamaged = 0
# for line in report:
#     if line[1] > line[0]:
#         for i in range(len(line)-1):
#             diff = line[i+1] - line[i]
#             if (diff < 1) or (diff > 3):
#                 numDamaged += 1
#                 break
#
#     else:
#         for i in range(len(line)-1):
#             diff = line[i] - line[i+1]
#             if (diff < 1) or (diff > 3):
#                 numDamaged += 1
#                 break

# print("Number of safe reports: ", len(report) - numDamaged)

# --------------- PART 2 -----------------

def is_safe(levels):
    inc = all(0 < y - x <= 3 for x, y in zip(levels, levels[1:]))
    dec = all(0 < x - y <= 3 for x, y in zip(levels, levels[1:]))
    return inc or dec

safe_count = 0

for level in report:
    if is_safe(level):
        safe_count += 1
    else:
        for i in range(len(level)):
            candidate = level[0:i] + level[i+1:]
            if is_safe(candidate):
                safe_count += 1
                break

print("Number of safe reports: ", safe_count)

