grid = []
with open('inputs/aoc_6_test') as f:
    for line in f:
        grid.append(list(line.rstrip('\n')))

def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                return r, c
    raise ValueError("no '^' in grid")

r, c = find_start(grid)

directions = {'up':'right', 'right':'down', 'down':'left', 'left':'up'}

r_num = len(grid)
c_num = len(grid[0])

def in_bounds (row, col, num_row, num_col):
    return 0 <= row < num_row and 0 <= col < num_col

dir = 'up'
result = 0
while True:
    r_next = c_next = 0
    if dir == 'up':
        r_next = r - 1
        c_next = c
    if dir == 'right':
        r_next = r
        c_next = c + 1
    if dir == 'down':
        r_next = r + 1
        c_next = c
    if dir == 'left':
        r_next = r
        c_next = c - 1
    if not in_bounds(r_next, c_next, r_num, c_num):
        break
    if grid[r_next][c_next] == '#':
        dir = directions[dir]
    else:
        r, c = r_next, c_next
        if grid[r][c] != 'X':
            grid[r][c] = 'X'
            result += 1

print(result)
with open("./inputs/aoc_6_results.txt", "w") as file:
    for line in grid:
        file.write(''.join(line))
        file.write('\n')

