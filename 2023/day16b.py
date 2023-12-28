# https://adventofcode.com/2023/day/16

import numpy as np


# with open("day16_input copy.txt") as file:
with open("day16_input.txt") as file:
	text = file.read().splitlines()

w = len(text[0])
h = len(text)

grid = np.full((w, h), ".")

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

def print_energy(grid, energized):
	copy = np.copy(grid)
	for e in energized:
		copy[e[0], e[1]] = "#"

	list_of_strings = [''.join(row) for row in copy.T.tolist()]
	print("\n".join(list_of_strings))
	print()

def get_energy(start_ray):
	start = np.copy(start_ray[0])
	beamed_dirs = [[[] for y in range(h)] for x in range(w)]
	rays = [start_ray]
	energized = set()

	while(len(rays) > 0):
		ray = rays.pop()

		while(True):
			next = ray[0] + ray[1]

			if not is_in_grid(next):
				break

			ray[0] = next

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

	print(start, len(energized))
	# print_energy(grid, energized)
	return len(energized)


max_energy = 0
for y in range(h):
	max_energy = max(max_energy, get_energy([np.array([-1, y]), np.array([1, 0])]))
	max_energy = max(max_energy, get_energy([np.array([w, y]), np.array([-1, 0])]))
for y in range(w):
	max_energy = max(max_energy, get_energy([np.array([y, -1]), np.array([0, 1])]))
	max_energy = max(max_energy, get_energy([np.array([y, h]), np.array([0, -1])]))


print(max_energy)