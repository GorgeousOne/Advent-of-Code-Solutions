# https://adventofcode.com/2023/day/9

import re
import numpy as np


def get_next(row):
	diffs = [row[i + 1] -row[i] for i in range(len(row) - 1)]
	if all(i == 0 for i in diffs):
		return row[-1]
	return row[-1] + get_next(diffs)



# with open("day09_input copy.txt") as file:
with open("day09_input.txt") as file:
	text = file.read().splitlines()

sums = 0
for i, line in enumerate(text):
	print(line)
	row = [int(s) for s in line.split()]
	sums += get_next(row)

print(sums)
