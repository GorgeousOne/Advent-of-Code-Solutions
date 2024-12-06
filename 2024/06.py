"""
https://adventofcode.com/2024/day/6
a guard walks on a square game field, turning right in front of obstacles, until they leave the field.
find out all unique positions of the guard, before they leave the field.
"""
import re
import numpy as np

# with open("06test.txt", "r") as f:
with open("06input.txt", "r") as f:
	t = f.read().splitlines()

field = np.zeros((len(t[0]), len(t)), dtype=np.int64)
dirs = np.array([
	[0, -1],
	[1, 0],
	[0, 1],
	[-1, 0]
])

for y, l in enumerate(t):
	for x, c in enumerate(l):
		if c == '#':
			field[x,y] = 1
		elif c == '^':
			g = np.array([x, y], dtype=np.int64)

d = dirs[0]
i = 0
steps = 0
path = set()

while g[0] >= 0 and g[0] < field.shape[0] and g[1] >= 0 and g[1] < field.shape[1]:
	path.add(tuple(g))
	fw = g + d
	# print(fw)
	if fw[0] >= 0 and fw[0] < field.shape[0] and fw[1] >= 0 and fw[1] < field.shape[1]:
		if 1 == field[tuple(fw)]:
			i += 1
			i %= 4
			d = dirs[i]
			# print("turn")
		else:
			# print("walk")
			g = fw
	else:
		break

print(len(path))

