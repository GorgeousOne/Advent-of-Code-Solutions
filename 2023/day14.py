# Day 14

import re
import numpy as np

with open("day14_input copy.txt") as file:
# with open("day14_input.txt") as file:
	text = file.read().splitlines()

w = len(text[0])
h = len(text)
field = np.zeros((w, h), dtype=int)

for y, line in enumerate(text):
	for x, letter in enumerate(line):
		if letter == "#":
			field[x,y] = 1
		elif letter == "O":
			field[x,y] = 2

def roll_x(field, x, y, dx):
	maxx = 0 if dx < 0 else x
	minx = field.shape[0] if dx < 0 else x

	for i in range(minx, maxx, dx):
		if field[i + dx, y] != 0:
			break
		field[i, y] = 0
		field[i + dx, y] = 2

def roll_y(field, x, y, dy):
	maxy = 0 if dy < 0 else y
	miny = field.shape[1] if dy < 0 else y

	for i in range(miny, maxy, dy):
		# print("check", i-1, field[x,i-1])
		if field[x,i-1] != 0:
			break
		field[x, i] = 0
		field[x, i - 1] = 2


for y in range(h):
	for x in range(w):
		if field[x,y] == 2:
			roll_y(field, x, y, -1)

sums = 0

for y in range(h):
	for x in range(w):
		if field[x,y] == 2:
			sums += h - y

print(sums)

signs = [".", "#", "O"]
for y in range(h):
	for x in range(w):
		print(signs[field[x,y]], end="")
	print()
