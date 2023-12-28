# https://adventofcode.com/2023/day/12

import re
import numpy as np

# with open("day12_input copy.txt") as file:
with open("day12_input.txt") as file:
	text = file.read().splitlines()

def space(x):
	return print(" " * x, end="")

def get_left_row(row, start):
	last_free = False
	for i, letter in enumerate(row[start:]):
		if last_free and letter != ".":
			return start + i
		last_free = letter != "#"
	return -1

def is_not_hash(row, i):
	return i < 0 or i >= len(row) or row[i] != "#"

def get_pattern_num(row, pattern, indent=0):
	min_chars = sum(pattern) + len(pattern) - 1

	if (len(row) < min_chars):
		return 0
	next = pattern[0]
	sums = 0
	last_width = len(row) - min_chars + 1

	for i in range(0, last_width):
		if is_not_hash(row, i-1) and is_not_hash(row, i+next) and "." not in row[i:i+next]:
			# space(indent)
			# print(row[0:i] + "■"*next + row[i+next:])
			if len(pattern) == 1:
				if "#" not in row[i+next:]:
					# space(indent)
					# print("X")
					sums += 1
			else:
				new_start = get_left_row(row, i + next)
				if new_start != -1:
					sums += get_pattern_num(row[new_start:], pattern[1:], indent + new_start)
		if row[i] == "#":
			break
	return sums


rows = []
patterns = []

for i, line in enumerate(text):
	parts = line.split()
	rows.append(parts[0])
	patterns.append([int(x) for x in parts[1].split(",")])

# idx = 2
# print(rows[idx], patterns[idx])
# print(get_pattern_num(rows[idx], patterns[idx]))

sums = 0
for i, pattern in enumerate(patterns):
	row = rows[i]
	col_idx = 0
	# print(get_pattern_num(row, pattern))
	sums += get_pattern_num(row, pattern)
print(sums)

