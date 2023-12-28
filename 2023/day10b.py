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

def neg(dir):
	return tuple(-dir[i] for i in range(len(dir)))

width = len(text[0])
height = len(text)

start_x = -1
start_y = -1
for i, line in enumerate(text):
	if "S" in line:
		start_y = i
		start_x = line.find("S")

start_dirs = []

if start_x < width-1 and text[start_y][start_x + 1] in ("-", "7", "J"):
	start_dirs.append((1, 0))
if start_x > 0 and text[start_y][start_x - 1] in ("-", "F", "L"):
	start_dirs.append((-1, 0))
if start_y < height-1 and text[start_y + 1][start_x] in ("|", "L", "J"):
	start_dirs.append((0, 1))
if start_y > 0 and text[start_y - 1][start_x] in ("|", "F", "7"):
	start_dirs.append((0, -1))
dirs["S"] = start_dirs

open_end = (start_x, start_y)
prev_dir = (0, 0)
loop = [open_end]

while True:
	coord = open_end
	pipe = text[coord[1]][coord[0]]
	loop_closed = False

	for pipe in dirs[pipe]:
		if neg(pipe) == prev_dir:
			continue

		neigh_x = coord[0] + pipe[0]
		neigh_y = coord[1] + pipe[1]

		if text[neigh_y][neigh_x] == "S":
			loop_closed = True
			break
		loop.append((neigh_x, neigh_y))
		open_end = (neigh_x, neigh_y)
		prev_dir = pipe
		break

	if loop_closed:
		break

insides = []

for y in range(height):
	intersecs = 0
	entry = 0
	for x in range(width):
		if not (x, y) in loop:
			if intersecs % 2 == 1:
				insides.append((x, y))
			continue

		pipe = text[y][x]
		if pipe == "-":
			continue
		if pipe == "|":
			intersecs += 1
			continue
		for dir in dirs[pipe]:
			if dir[1] == 0:
				continue
			if entry == 0:
				intersecs += 1
				entry = dir[1]
			else:
				if dir[1] == entry:
					intersecs += 1
				entry == 0
			break

vis = {
	"F": "┏",
	"-": "━",
	"7": "┓",
	"|": "┃",
	"J": "┛",
	"L": "┗",
	"S": "S"
}

for y in range(height):
	for x in range(width):
		if (x, y) in insides:
			print("█", end="")
		elif (x, y) in loop:
			print(vis[text[y][x]], end="")
		else:
			print("░" if text[y][x] == "." else " ", end="")
	print()

print(len(insides))
