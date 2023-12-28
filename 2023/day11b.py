# https://adventofcode.com/2023/day/11

import re
import math

# with open("day11_input copy.txt") as file:
with open("day11_input.txt") as file:
	text = file.read().splitlines()

mil = 999999
def addRow(row, empty_rows, stars):
	for k, other in enumerate(empty_rows):
		if other > row:
			empty_rows[k] = other + mil
	for k, star in enumerate(stars):
		if star[0] > row:
			stars[k] = (star[0] + mil, star[1])

def addCol(col, empty_cols, stars):
	for k, other in enumerate(empty_cols):
		if other > col:
			empty_cols[k] = other + mil
	for k, star in enumerate(stars):
		if star[1] > col:
			stars[k] = (star[0], star[1] + mil)

space = []
for i, line in enumerate(text):
	space.append([letter for letter in line])

stars = []
w = len(space[0])
h = len(space)

for y in range(h):
	for x in range(w):
		if space[y][x] == "#":
			stars.append((y, x))


empty_rows = []
empty_cols = []

for i in range(w):
	is_empty = all(letter == "." for letter in space[i])
	if is_empty:
		empty_rows.append(i)

for j in range(h):
	col = [row[j] for row in space]
	is_empty = all(letter == "." for letter in col)
	if is_empty:
		empty_cols.append(j)


for i in range(len(empty_rows)):
	addRow(empty_rows[i], empty_rows, stars)
for j in range(len(empty_cols)):
	addCol(empty_cols[j], empty_cols, stars)


sums = 0

for i in range(len(stars) - 1):
	for j in range(i+1, len(stars)):
		star1 = stars[i]
		star2 = stars[j]
		dist = abs(star2[0] - star1[0]) + abs(star2[1] - star1[1])
		sums += dist

print(sums)