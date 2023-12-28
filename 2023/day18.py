# https://adventofcode.com/2023/day/18

import re
import numpy as np

# with open("day18_input copy.txt") as file:
with open("day18_input.txt") as file:
	text = file.read().splitlines()

size = 10000
field = np.zeros((2*size, 2*size))
current = np.array([size, size])

dirs = {
	"L": np.array([-1, 0]),
	"R": np.array([1, 0]),
	"D": np.array([0, 1]),
	"U": np.array([0, -1])
}

holes = 0

for i, line in enumerate(text):
	parts = line.split()
	dir = dirs[parts[0]]
	times = int(parts[1])

	for i in range(times):
		next = current + dir
		if (field[next[0], next[1]] != 1):
			field[next[0], next[1]] = 1
			holes += 1
		current = next

print("trench", holes)
ends = [np.array([size + 1, size + 1])]

while (len(ends) > 0):
	current = ends.pop()

	for dir in dirs.values():
		next = current + dir
		if field[next[0], next[1]] != 1:
			field[next[0], next[1]] = 1
			ends.append(next)
			holes += 1


print("lagoon", holes)
