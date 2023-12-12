# Day 12

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

solitions = {}

def get_pattern_num(row, pattern, indent=0):
	problem = (row, tuple(pattern))
	solition = solitions.get(problem, -1)

	if solition != -1:
		return solition

	good_chars = len(row) - row.count(".")
	if good_chars < sum(pattern):
		return 0
	next = pattern[0]
	sums = 0
	
	min_chars = sum(pattern) + len(pattern) - 1
	last_width = len(row) - min_chars + 1

	for i in range(0, last_width):
		if is_not_hash(row, i-1) and is_not_hash(row, i+next) and "." not in row[i:i+next]:
			if len(pattern) == 1:
				if "#" not in row[i+next:]:
					sums += 1
			else:
				new_start = get_left_row(row, i + next)
				if new_start != -1:
					sums += get_pattern_num(row[new_start:], pattern[1:], indent + new_start)
		if row[i] == "#":
			break
	solitions[problem] = sums
	return sums


rows = []
patterns = []

for i, line in enumerate(text):
	parts = line.split()
	# springs.append([x for x in parts[0]])
	rows.append("?".join([parts[0] for _ in range(5)]))
	patterns.append([int(x) for x in parts[1].split(",")] * 5)

sums = 0
from tqdm import tqdm

for i in range(len(rows)):
	pattern = patterns[i]
	row = rows[i]
	col_idx = 0
	sums += get_pattern_num(row, pattern)
print(sums)
