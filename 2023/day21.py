# https://adventofcode.com/2023/day/21

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
all_reached = set()
last_reached = set()

final_reach.add(start)
all_reached.add(start)
last_reached.add(start)

steps = 1000

for i in range(1, steps + 1):
	next_reached = set()

	for point in last_reached:
		loc = np.array(point)

		for dir in dirs:
			next = tuple(loc + dir)

			if garden[next[0], next[1]] == 1:
				continue

			if next in all_reached:
				continue

			next_reached.add(next)
			all_reached.add(next)

			if i % 2 == 0:
				final_reach.add(next)

	last_reached = next_reached

print(len(final_reach))