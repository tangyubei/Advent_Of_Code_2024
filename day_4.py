data = []
with open('./inputs/aoc_4.txt', 'r') as f:
    for line in f:
        newLine = ['0','0','0']+list(line.strip())+['0','0','0']
        # newLine = list(line.strip())
        data.append(newLine)

testData = [
    ['0','0','0','M','M','M','S','X','X','M','A','S','M','0','0','0'],
['0','0','0','M','S','A','M','X','M','S','M','S','A','0','0','0'],
['0','0','0','A','M','X','S','X','M','A','A','M','M','0','0','0'],
['0','0','0','M','S','A','M','A','S','M','S','M','X','0','0','0'],
['0','0','0','X','M','A','S','A','M','X','A','M','M','0','0','0'],
['0','0','0','X','X','A','M','M','X','X','A','M','A','0','0','0'],
['0','0','0','S','M','S','M','S','A','S','X','S','S','0','0','0'],
['0','0','0','S','A','X','A','M','A','S','A','A','A','0','0','0'],
['0','0','0','M','A','M','M','M','X','M','M','M','M','0','0','0'],
['0','0','0','M','X','M','X','A','X','M','A','S','X','0','0','0']]

def count_XMAS(grid):
    patterns = {'XMAS', 'SAMX'}
    R, C = len(grid), len(grid[0])
    pad = 3


    P = [['0'] * (C + 2*pad) for _ in range(pad)]
    for row in grid:
        P.append(['0']*pad + row + ['0']*pad)
    P += [['0'] * (C + 2*pad) for _ in range(pad)]

    count = 0
    for i in range(pad, pad+R):
        for j in range(pad, pad+C):

            if ''.join(P[i][j+k] for k in range(4)) in patterns:
                count += 1

            if ''.join(P[i+k][j]   for k in range(4)) in patterns:
                count += 1

            if ''.join(P[i+k][j+k] for k in range(4)) in patterns:
                count += 1

            if ''.join(P[i+k][j-k] for k in range(4)) in patterns:
                count += 1

    return count

print(count_XMAS(data))

