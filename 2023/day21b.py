# Day 21

import re
import numpy as np

# with open("day21_input copy.txt") as file:
with open("day21_input.txt") as file:
	text = file.read().splitlines()

w = len(text[0])
h = len(text)
garden = np.zeros((w, h), dtype=int)

for y, line in enumerate(text):
	for x, letter in enumerate(line):
		if letter == "#":
			garden[x, y] = 1
		elif letter == "S":
			start = (x, y)

dirs = [
	np.array([-1, 0]),
	np.array([1, 0]),
	np.array([0, 1]),
	np.array([0, -1])
]

def wrap_pos(pos, max_x, max_y):
	return (pos[0] % max_x, pos[1] % max_y)

final_reach = set()

print(w, h)

steps = 26501365

square_reach = (steps - 65) // w

n = square_reach - 1
fulls = (n * (n + 1) * (2 * n + 1)) // 6
# print(fulls)

all_count = np.count_nonzero(garden)

counts1 = 0
counts2 = 0
counts3 = 0
counts4 = 0
for x in range(65):
	for y in range(65 - x):
		if garden[x, y] == 1:
			counts1 += 1
		if garden[w - 1 - x, y] == 1:
			counts2 += 1
		if garden[w - 1 - x, h - 1 - y] == 1:
			counts3 += 1
		if garden[x, h - 1 - y] == 1:
			counts4 += 1

print(counts1, counts2, counts3, counts4)
