from collections import defaultdict

left_locations = []
right_locations = []
with open("inputs/aoc_1.txt") as f:
    for line in f:
      left_locations.append(int(line.split()[0]))
      right_locations.append(int(line.split()[1]))

# --------------- PART 1 -----------------
result = 0

left_locations.sort()
right_locations.sort()

for i in range(len(left_locations)):
    result += abs(left_locations[i] - right_locations[i])

print(result) #ANSWER: 2_113_135

# --------------- PART 2 -----------------
r_dict = defaultdict(int)

for id in right_locations:
    r_dict[id] += 1

similarity_score = 0
for id in left_locations:
    similarity_score += id * r_dict[id]
print(similarity_score) # 19_097_157