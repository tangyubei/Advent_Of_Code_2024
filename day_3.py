import re
# --------------- PART 1 -----------------
testInput = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
with open('./inputs/aoc_3.txt', 'r') as f:
    data = f.read()
#
# matches = re.findall(('mul\(\d+,\d+\)'), data)
# result = 0
#
# for entry in matches:
#     y = list(map(int, re.findall('(\d+)', entry)))
#     result += y[0] * y[1]
#
# print(result)

# --------------- PART 2 -----------------
part_2_test_input = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'

print("length of instructions", len(part_2_test_input))
def readInstructions(instructions):
    result = 0
    while instructions:
        nextDontIndex = instructions.find('don\'t()')
        matches = re.findall(('mul\(\d+,\d+\)'), instructions[:nextDontIndex])
        for entry in matches:
            y = list(map(int, re.findall('(\d+)', entry)))
            result += y[0] * y[1]
        nextDoIndex = instructions[nextDontIndex:].find('do()')
        if nextDoIndex == -1:
            return result
        instructions = instructions[nextDontIndex + nextDoIndex + 1:]
    return None


print(readInstructions(data))
