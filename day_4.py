from collections import Counter

data = []
with open('./inputs/aoc_4.txt', 'r') as file:
    for line in file:
        data.append(list(line.strip()))

# --------------- PART 1 -----------------
# x_max = len(data[0])
# y_max = len(data)
#
# # Padding the data
# for r in data:
#     r.extend(['0', '0', '0'])
#
# for _ in range(3):
#     data.append(['0']*(x_max+3))
#
# def count_xmas(grid):
#     count = 0
#     for i in range(y_max):
#         for j in range(x_max):
#             if ''.join([grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3]]) in {'XMAS', 'SAMX'}:
#                 count += 1
#             if ''.join([grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]]) in {'XMAS', 'SAMX'}:
#                 count += 1
#             if ''.join([grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]]) in {'XMAS', 'SAMX'}:
#                 count += 1
#             if ''.join([grid[i][j], grid[i + 1][j - 1], grid[i + 2][j - 2], grid[i + 3][j - 3]]) in {'XMAS', 'SAMX'}:
#                 count += 1
#     return count
#
# print(count_xmas(data))

# --------------- PART 2 -----------------
print(data)
x_max = len(data[0])
y_max = len(data)

# Padding the data
new_data = [['0']*(x_max+2)]
for r in data:
    l = ['0']+r+['0']
    new_data.append(l)
new_data.append(['0']*(x_max+2))

def rotate(l, n):
    return l[n:] + l[:n]

def count_xmas_updated(data):
    target = ['M','M','S','S']
    count = 0
    for i in range(1, y_max+1):
        for j in range(1, x_max+1):
            if new_data[i][j] == 'A':
                    test = [new_data[i-1][j-1], new_data[i-1][j+1], new_data[i+1][j+1], new_data[i+1][j-1]]
                    for _ in range(4):
                        if test == rotate(target, _):
                            count += 1
    return count

print(count_xmas_updated(data))
