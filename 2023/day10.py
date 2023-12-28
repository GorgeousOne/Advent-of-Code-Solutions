# https://adventofcode.com/2023/day/10

import re
import numpy as np

# with open("day10_input copy.txt") as file:
with open("day10_input.txt") as file:
	text = file.read().splitlines()


dirs = {
	".": [],
	"F": [(0, 1), (1, 0)],
	"-": [(-1, 0), (1, 0)],
	"7": [(-1, 0), (0, 1)],
	"|": [(0, -1), (0, 1)],
	"J": [(0, -1), (-1, 0)],
	"L": [(0, -1), (1, 0)],
}

width = len(text[0])
height = len(text)
dists = [[-1 for i in range(width)] for j in range(height)]

start_x = -1
start_y = -1
for i, line in enumerate(text):
	if "S" in line:
		start_y = i
		start_x = line.find("S")

start_dirs = []

if text[start_y][start_x + 1] in ("-", "7", "J"):
	start_dirs.append((1, 0))
if text[start_y][start_x - 1] in ("-", "F", "L"):
	start_dirs.append((-1, 0))
if text[start_y + 1][start_x] in ("|", "L", "J"):
	start_dirs.append((0, 1))
if text[start_y][start_x + 1] in ("|", "F", "7"):
	start_dirs.append((0, -1))
dirs["S"] = start_dirs

print(start_dirs)
open_ends = {(start_x, start_y)}
dists[start_y][start_x] = 0

while len(open_ends) > 0:
	coord = open_ends.pop()
	pipe = text[coord[1]][coord[0]]
	dist = dists[coord[1]][coord[0]]

	for dir in dirs[pipe]:
		neigh_x = coord[0] + dir[0]
		neigh_y = coord[1] + dir[1]

		if neigh_x < 0 or neigh_x >= width or neigh_y < 0 or neigh_y > height:
			continue
		if text[neigh_y][neigh_x] not in dirs.keys():
			continue
		neigh_dist = dists[neigh_y][neigh_x]

		if neigh_dist == -1 or neigh_dist > dist + 1:
			open_ends.add((neigh_x, neigh_y))
			dists[neigh_y][neigh_x] = dist + 1

print(max(max(row) for row in dists))

# space = 3
# for y in range(height):
# 	for x in range(width):
# 		dist = dists[y][x]
# 		print(".".ljust(space) if dist == -1 else str(dist).ljust(space), end="")
# 	print("\n")