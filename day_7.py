import re
from itertools import product
import math
import time

equations = []
with open('inputs/aoc_7.txt') as file:
    for f in file:
        line = re.split('\D',f)
        equations.append([int(x) for x in line if x != '' ])

# --------------- PART 1 -----------------

# def operator_sequences(n):
#     return [list(p) for p in product('*+', repeat=n)]
#
# def check_valid_equation(equation):
#     result = equation[0]
#     operands = equation[1:]
#     sequences = operator_sequences(len(operands)-1)
#     for s in sequences:
#         candidate = operands[0]
#         for i in range(1,len(operands)):
#             if s[i-1] == '+':
#                 candidate += operands[i]
#             else:
#                 candidate *= operands[i]
#         if candidate == result:
#             return candidate
#     return False
#
# calibration_result = 0
# for equation in equations:
#     calibration_result += check_valid_equation(equation)
# print(calibration_result)

# --------------- PART 2 -----------------
#
# def operator_sequences(n):
#     return [list(p) for p in product('*+|', repeat=n)]
#
# def concatenate_digits(a, b):
#     digits = int(math.log10(b)) + 1
#     a = a * (10 ** digits)
#     return a + b
#
# def check_valid_equation(equation):
#     result = equation[0]
#     operands = equation[1:]
#     sequences = operator_sequences(len(operands)-1)
#     for s in sequences:
#         candidate = operands[0]
#         for i in range(1,len(operands)):
#             if s[i-1] == '+':
#                 candidate += operands[i]
#             elif s[i-1] == '*':
#                 candidate *= operands[i]
#             else:
#                 candidate = concatenate_digits(candidate, operands[i])
#         if candidate == result:
#             return candidate
#     return False
#
# calibration_result = 0
#
# start_time = time.time()
# for equation in equations:
#     calibration_result += check_valid_equation(equation)
# print(calibration_result)
# print("--- %s seconds ---" % (time.time() - start_time))

# --------------- PART 2 (with speed-up) -----------------


def operator_sequences(n):
    return [list(p) for p in product('*+|', repeat=n)]

def concatenate_digits(a, b):
    digits = int(math.log10(b)) + 1
    a = a * (10 ** digits)
    return a + b

def check_valid_equation(equation):
    result = equation[0]
    operands = equation[1:]
    sequences = operator_sequences(len(operands)-1)
    for s in sequences:
        candidate = operands[0]
        for i in range(1,len(operands)):
            if s[i-1] == '+':
                candidate += operands[i]
            elif s[i-1] == '*':
                candidate *= operands[i]
            else:
                candidate = concatenate_digits(candidate, operands[i])
        if candidate == result:
            return candidate
    return False

calibration_result = 0

start_time = time.time()
for equation in equations:
    calibration_result += check_valid_equation(equation)
print(calibration_result)
print("--- %s seconds ---" % (time.time() - start_time))