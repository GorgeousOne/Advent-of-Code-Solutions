# https://adventofcode.com/2023/day/11

import re
import numpy as np
import math

# with open("day11_input copy.txt") as file:
with open("day11_input.txt") as file:
	text = file.read().splitlines()

def addRow(space, i):
	space.insert(i, ["." for k in range(len(space[0]))])

def addCol(space, j):
	for row in space:
		row.insert(j, ".")

space = []
for i, line in enumerate(text):
	space.append([letter for letter in line])

i = 0
while(i < len(space)):
	is_empty = all(letter == "." for letter in space[i])
	if is_empty:
		addRow(space, i)
		i += 1
	i += 1


j = 0
while(j < len(space[0])):
	col = [row[j] for row in space]
	is_empty = all(letter == "." for letter in col)
	if is_empty:
		addCol(space, j)
		j += 1
	j += 1

stars = []
w = len(space[0])
h = len(space)

for y in range(h):
	for x in range(w):
		if space[y][x] == "#":
			stars.append((y, x))

sums = 0

for i in range(len(stars) - 1):
	for j in range(i+1, len(stars)):
		star1 = stars[i]
		star2 = stars[j]
		dist = abs(star2[0] - star1[0]) + abs(star2[1] - star1[1])
		# print(i+1, j+1, ":", dist)
		sums += dist

print(sums)