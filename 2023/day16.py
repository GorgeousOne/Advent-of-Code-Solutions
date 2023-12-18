# Day 16

import numpy as np


# with open("day16_input copy.txt") as file:
with open("day16_input.txt") as file:
	text = file.read().splitlines()

w = len(text[0])
h = len(text)

grid = np.full((w, h), ".")
beamed_dirs = [[[] for y in range(h)] for x in range(w)]

for y, line in enumerate(text):
	for x, letter in enumerate(line):
		grid[x,y] = letter


splitters = {
	"|": np.array([0, 1]),
	"-": np.array([1, 0])
}

redirects = {
	"/": [
		[np.array([1, 0]), np.array([0, -1])],
		[np.array([-1, 0]), np.array([0, 1])],
		[np.array([0, 1]), np.array([-1, 0])],
		[np.array([0, -1]), np.array([1, 0])]
		],
	"\\": [
		[np.array([1, 0]), np.array([0, 1])],
		[np.array([-1, 0]), np.array([0, -1])],
		[np.array([0, 1]), np.array([1, 0])],
		[np.array([0, -1]), np.array([-1, 0])]
		]
}

def is_ortho(dir1, dir2):
	return abs(dir1[0]) != abs(dir2[0])

def get_redirect(dir, letter):
	for redir in redirects[letter]:
		if np.array_equal(dir, redir[0]):
			return redir[1]

def get_splits(dir, letter):
	splitDir = splitters[letter]
	if is_ortho(dir, splitDir):
		return [splitDir, -splitDir]
	return [dir]

def is_in_grid(coord):
	return coord[0] >= 0 and coord[0] < w and coord[1] >= 0 and coord[1] < h


rays = [[np.array([-1, 0]), np.array([1, 0])]]
energized = set()

while(len(rays) > 0):
	ray = rays.pop()
	
	while(True):
		next = ray[0] + ray[1]

		if not is_in_grid(next):
			break

		ray[0] = next
		# time.sleep(0.5)

		if tuple(ray[1]) in beamed_dirs[ray[0][0]][ray[0][1]]:
			break
		beamed_dirs[next[0]][next[1]].append(tuple(ray[1]))

		energized.add(tuple(next))
		letter = grid[next[0], next[1]]


		if letter in splitters:
			for redir in get_splits(ray[1], letter):
				rays.append([next, redir])
			break
		elif letter in redirects:
			ray[1] = get_redirect(ray[1], letter)

for e in energized:
	grid[e[0], e[1]] = "#"

list_of_strings = [''.join(row) for row in grid.T.tolist()]
print("\n".join(list_of_strings))
print(len(energized))