"""
https://adventofcode.com/2024/day/7
read in all formulas: "result: operand operand operand..."
and check which ones produce the correct result by adding combinations of operators
like +, * or in part 2 '|' (concatenates both operands).
All operands are evaluated from left to right only.
"""

import re
import numpy as np

# with open("07test.txt", "r") as f:
with open("07input.txt", "r") as f:
	t = f.read().splitlines()

def calc(goodset, check, sum, ops, next_op, d):
	# print("  " * d + "test", next_op, ops[0])
	if next_op == '+':
		sum += ops[0]
	elif next_op == '*':
		sum *= ops[0]
	else:
		sum = int(str(sum) + str(ops[0]))

	if sum > check:
		return

	if len(ops) <= 1:
		if check == sum:
			goodset.add(check)
		# print("--add", check)
		return

	calc(goodset, check, sum, ops[1:], '+', d+1)
	calc(goodset, check, sum, ops[1:], '*', d+1)
	calc(goodset, check, sum, ops[1:], '|', d+1)


goods = set()

for l in t:
	c = l.split(': ')
	ccheck = int(c[0])
	ops = [int(x) for x in c[1].split()]
	# print()
	# print(ccheck, ops)
	calc(goods, ccheck, ops[0], ops[1:], '+', 0)
	calc(goods, ccheck, ops[0], ops[1:], '*', 0)
	calc(goods, ccheck, ops[0], ops[1:], '|', 0)

# print(goods)
print(sum(goods))