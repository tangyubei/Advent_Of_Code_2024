import re
# --------------- PART 1 -----------------
# test = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
with open('./inputs/aoc_3.txt', 'r') as f:
    data = f.read()

# --------------- PART 1 -----------------
def mul(substring):
    matches = re.findall('mul\(\d+,\d+\)', substring)
    result = 0
    for m in matches:
        operands = [int(x) for x in re.findall('\d+',m)]
        result += operands[0] * operands[1]
    return result

# --------------- PART 2 -----------------
test = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
def updated_mul(text):
    r = 0
    while True:
        i = text.find('don\'t()')
        if i == -1:
            r += mul(text)
            break
        target_string = text[:i]
        r += mul(target_string)
        j = text.find('do()', i + len("don't()"))
        if j == -1:
            break
        text = text[j+4:]
    return r

print(updated_mul(data))
