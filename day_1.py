from collections import defaultdict

# --------------- PART 1 -----------------
leftInput, rightInput = [], []
with open('./inputs/aoc_1.txt', 'r') as file:
    for line in file:
        newLine = list(line.rstrip('\n').split())
        leftInput.append(int(newLine[0]))
        rightInput.append(int(newLine[1]))

leftInput.sort()
rightInput.sort()

distance = 0
for i in range(len(leftInput)):
    distance += abs(leftInput[i] - rightInput[i])

print(distance)

# --------------- PART 2 -----------------
rightDict = defaultdict(int)
for num in rightInput:
    rightDict[num] += 1

similarityScore = 0
for num in leftInput:
    similarityScore += num * rightDict[num]

print(similarityScore)