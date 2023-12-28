# https://adventofcode.com/2023/day/13

import re
import numpy as np

# with open("day13_input copy.txt") as file:
with open("day13_input.txt") as file:
	text = file.read().splitlines()

pattern_rows = []
pattern_cols = []
rows = []

for i, line in enumerate(text):
	if line == "":
		# print("space", i)
		cols = ["".join([rows[row][col] for row in range(len(rows))]) for col in range(len(rows[0]))]
		pattern_rows.append(rows)
		pattern_cols.append(cols)
		rows = []
		continue
	rows.append(line)

def get_mirror_i(pattern):
	mirror_i = -1
	size = len(pattern)

	for start in range(0, size - 1):
		is_mirror = True
		max_delta = min(start + 1, size - 1 - start)

		for delta in range(max_delta):
			if pattern[start - delta] != pattern[start + 1 + delta]:
				is_mirror = False
				break
		if is_mirror:
			mirror_i = start
			break
	return mirror_i

sums = 0

for i in range(len(pattern_cols)):

	rows = pattern_rows[i]
	cols = pattern_cols[i]
	mirror_y = get_mirror_i(rows)

	if mirror_y != -1:
		sums += 100 * (mirror_y + 1)
		continue

	mirror_x = get_mirror_i(cols)

	if mirror_x != -1:
		sums += mirror_x + 1
	else:
		print("meh", i)

print(sums)

